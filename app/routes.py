from flask import Blueprint, render_template, url_for, request
from .models import Vehicle

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

@main.route('/vehicles', methods=['GET'])
def vehicles():
    make = request.args.get('make', 'any')
    model = request.args.get('model', 'any')
    year = request.args.get('year', 'any')
    mileage = request.args.get('mileage', 'any')
    top_speed = request.args.get('top_speed', 'any')
    acceleration = request.args.get('acceleration', 'any')
    price = request.args.get('price', 'any')
    color = request.args.get('color', 'any')

    query = Vehicle.query

    if make != 'any':
        query = query.filter_by(make=make)
    if model != 'any':
        query = query.filter_by(model=model)
    if year != 'any':
        query = query.filter_by(year=int(year))
    if mileage != 'any':
        query = query.filter(Vehicle.mileage <= int(mileage))
    if top_speed != 'any':
        query = query.filter(Vehicle.top_speed >= int(top_speed))
    if acceleration != 'any':
        query = query.filter(Vehicle.acceleration <= float(acceleration))
    if price != 'any':
        query = query.filter(Vehicle.price <= float(price))
    if color != 'any':
        query = query.filter_by(color=color)

    vehicles = query.all()

    makes = [v.make for v in Vehicle.query.distinct(Vehicle.make)]
    models = [v.model for v in Vehicle.query.distinct(Vehicle.model)]
    years = sorted({v.year for v in Vehicle.query.distinct(Vehicle.year)})
    mileage_options = [10000, 20000, 30000, 40000]
    top_speed_options = [150, 200, 250, 300]
    acceleration_options = [3.2, 5.6, 7.8]
    price_options = [30000, 40000, 50000]
    color_options = ['Red', 'Blue', 'Black']

    return render_template(
        'search.html',
        make=make,
        model=model,
        year=year,
        mileage_value=mileage,
        top_speed_value=top_speed,
        acceleration_value=acceleration,
        price_value=price,
        color=color,
        vehicles=vehicles,
        makes=makes,
        models=models,
        years=years,
        mileage=mileage_options,
        top_speed=top_speed_options,
        acceleration_options=acceleration_options,
        prices=price_options,
        colors=color_options
    )

@main.route('/contactus')
def contactus():
    return render_template('contactus.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/signup')
def signup():
    return render_template('signup.html')
