from flask import Blueprint, render_template, request, url_for, flash, redirect, current_app, session
from .models import Vehicle, Brand, Model
from .forms import SearchForm, AddListingForm
from . import db
from werkzeug.utils import secure_filename
from flask import jsonify
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

@main.route('/search', methods=['GET', 'POST'])
def search_vehicles():
    if request.method == 'POST':
        make_id = request.form.get('make')
        model_id = request.form.get('model')
        year = request.form.get('year')
        mileage = request.form.get('mileage')
        top_speed = request.form.get('top_speed')
        acceleration = request.form.get('acceleration')
        price = request.form.get('price')
        color = request.form.get('color')

        query = Vehicle.query.join(Brand).join(Model)

        if make_id != 'any':
            query = query.filter(Vehicle.make == make_id)
        if model_id != 'any':
            query = query.filter(Vehicle.model == model_id)
        if year != 'any':
            query = query.filter(Vehicle.year == year)
        if mileage != 'any':
            query = query.filter(Vehicle.mileage == mileage)
        if top_speed != 'any':
            query = query.filter(Vehicle.top_speed == top_speed)
        if acceleration != 'any':
            query = query.filter(Vehicle.acceleration == acceleration)
        if price != 'any':
            query = query.filter(Vehicle.price == price)
        if color != 'any':
            query = query.filter(Vehicle.color == color)

        vehicles = query.all()

        return render_template('search_results.html', vehicles=vehicles)

    brands = Brand.query.all()
    makes = [(brand.id, brand.name) for brand in brands]
    years = sorted(set(vehicle.year for vehicle in Vehicle.query.all()))
    mileages = sorted(set(vehicle.mileage for vehicle in Vehicle.query.all()))
    top_speeds = sorted(set(vehicle.top_speed for vehicle in Vehicle.query.all()))
    accelerations = sorted(set(vehicle.acceleration for vehicle in Vehicle.query.all()))
    prices = sorted(set(vehicle.price for vehicle in Vehicle.query.all()))
    colors = sorted(set(vehicle.color for vehicle in Vehicle.query.all()))

    return render_template('search.html', makes=makes, years=years, mileages=mileages, top_speeds=top_speeds, accelerations=accelerations, prices=prices, colors=colors)



@main.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    form = AddListingForm()

    # Populate brand choices
    form.make.choices = [(brand.id, brand.name) for brand in Brand.query.all()]

    # If a brand is selected, populate model choices based on the selected brand
    if form.make.data:
        form.model.choices = [(model.id, model.name) for model in Model.query.filter_by(brand_id=form.make.data).all()]
    else:
        form.model.choices = [(0, 'Select a model')]

    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(current_app.root_path, 'static/img', filename)
        image_file.save(image_path)
        new_vehicle = Vehicle(
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            mileage=form.mileage.data,
            battery_capacity=form.battery_capacity.data,
            color=form.color.data,
            price=form.price.data,
            doors=form.doors.data,
            car_type=form.car_type.data,
            top_speed=form.top_speed.data,
            acceleration=form.acceleration.data,
            image_url=url_for('static', filename='img/' + filename),
            seller_id=session['user_id']
        )
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Your listing has been added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_listing.html', form=form)

@main.route('/get_models/<int:brand_id>')
def get_models(brand_id):
    models = Model.query.filter_by(brand_id=brand_id).all()
    models_list = [{'id': model.id, 'name': model.name} for model in models]
    return jsonify(models_list)


@main.route('/contactus')
def contactus():
    return render_template('contactus.html')