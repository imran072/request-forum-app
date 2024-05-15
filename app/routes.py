from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .models import Vehicle, CarAd
from .forms import SearchForm
from . import db
import os

main = Blueprint('main', __name__)


@main.route('/')
def index():
    makes = ['Audi', 'Bentley', 'BMW', 'BYD', 'Chery', 'Chevrolet', 'Fiat', 'Fisker', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Kia', 'Lexus', 'Maserati', 'Mahindra', 'Mercedes-Benz', 'MG', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Opel', 'Renault', 'Suzuki', 'Tesla', 'Toyota', 'Volvo', 'Volkswagen']
    distances = [5, 10, 15, 20, 30, 40, 50, 75, 100, 150, 200]
    prices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    ads = [
        {'name': 'Tesla Model 3', 'price': 25000, 'description': 'Model 3 is designed for electric-powered performance, with quick acceleration, long range and fast charging.', 'image': 'Tesla_Model_3.png', 'alt': 'Tesla_Model_3'},
        {'name': 'Toyota Camry', 'price': 20000, 'description': 'Toyota Electrified - Towards the future', 'image': 'Toyota_Camry.png', 'alt': 'Toyota_Camry'},
        {'name': 'Tesla Model S', 'price': 28000, 'description': 'Model 3 is designed for electric-powered performance, with quick acceleration, long range and fast charging.', 'image': 'Tesla_Model_X.png', 'alt': 'Tesla_Model_S'}
    ]
    brand_logos = ['Tesla.png', 'Honda.png', 'Fisker.png', 'Ford.png', 'Audi.png', 'Renault.png', 'Toyota.png', 'Volvo.png', 'Maserati.png', 'Nissan.png', 'Mahindra.png', 'Kia.png', 'Jaguar.png', 'Hyundai.png', 'BYD.png', 'Volkswagen.png', 'Bentley.png', 'BMW.png']

    print(url_for('main.index'))
    return render_template('index.html', makes=makes, distances=distances, prices=prices, ads=ads, brand_logos=brand_logos)

@main.route('/vehicles')
def vehicles():
    makes = ['Audi', 'Bentley', 'BMW', 'BYD', 'Chery', 'Chevrolet', 'Fiat', 'Fisker', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Kia', 'Lexus', 'Maserati', 'Mahindra', 'Mercedes-Benz', 'MG', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Opel', 'Renault', 'Suzuki', 'Tesla', 'Toyota', 'Volvo', 'Volkswagen']
    years = list(range(2000, 2024))
    mileage = ['5000', '10000', '15000', '20000', '25000', '30000', '35000', '40000', '45000', '50000']
    top_speed = ['120', '150', '180', '200', '220', '240', '260']
    acceleration = ['3', '4', '5', '6', '7', '8', '9', '10']
    prices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Silver', 'Gray', 'Yellow']

    return render_template('search.html', makes=makes, years=years, mileage=mileage, top_speed=top_speed, acceleration=acceleration, prices=prices, colors=colors)

@main.route('/search_vehicles', methods=['POST'])
def search_vehicles():
    make = request.form.get('make')
    model = request.form.get('model')
    year = request.form.get('year', type=int)
    mileage = request.form.get('mileage', type=int)
    top_speed = request.form.get('top_speed', type=int)
    acceleration = request.form.get('acceleration', type=float)
    price = request.form.get('price', type=float)
    color = request.form.get('color')

    query = Vehicle.query
    if make and make != 'any':
        query = query.filter(Vehicle.make == make)
    if model and model != 'any':
        query = query.filter(Vehicle.model == model)
    if year and year != 'any':
        query = query.filter(Vehicle.year == year)
    if mileage and mileage != 'any':
        query = query.filter(Vehicle.mileage <= mileage)
    if top_speed and top_speed != 'any':
        query = query.filter(Vehicle.top_speed <= top_speed)
    if acceleration and acceleration != 'any':
        query = query.filter(Vehicle.acceleration <= acceleration)
    if price and price != 'any':
        query = query.filter(Vehicle.price <= price)
    if color and color != 'any':
        query = query.filter(Vehicle.color == color)

    vehicles = query.all()
    return render_template('search_results.html', vehicles=vehicles)

@main.route('/contactus')
def contactus():
    return render_template('contactus.html')

@main.route('/post_ad', methods=['POST'])
@login_required
def post_ad():
    if request.method == 'POST':
        # Retrieve all form data
        brand = request.form['brand']
        model = request.form['model']
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        file = request.files['image']

        if file and brand and model and title and description and price:
            filename = secure_filename(file.filename)
            # Construct a path to save the file (you might want to include more unique identifiers)
            filepath = os.path.join(main.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Create a new ad instance and save to the database
            new_ad = CarAd(
                brand=brand,
                model=model,
                title=title,
                description=description,
                price=price,
                image_path=filepath,
                user_id=current_user.id  # the user is logged in
            )
            db.session.add(new_ad)
            db.session.commit()

            flash('Your ad has been posted successfully!', 'success')
            return redirect(url_for('main.index'))  # Redirect to the user's profile page
        else:
            flash('All fields are required.', 'error')
            return redirect(url_for('add_listing'))  # Redirect back to the form if there are errors

    return render_template('add_listing.html', request=request)