from flask import Blueprint, render_template, request
from .models import Vehicle

main = Blueprint('main', __name__)

@main.route('/')
def index():
    makes = ['Tesla', 'BMW', 'Nissan']
    prices = [20000, 40000, 60000]
    distances = [100, 200, 300]

    ads = [
        {
            'name': 'Tesla Model S 100D Long Range',
            'price': 79995.0,
            'description': 'All Glass Panoramic Roof, Premium Interior and Lighting.',
            'image': 'tesla_model_s_100d_long_range.jpg',
            'alt': 'Tesla Model S 100D Long Range'
        },
        {
            'name': 'Tesla Model S E 85D',
            'price': 47995.0,
            'description': 'All Glass Panoramic Roof, Alloy Wheels.',
            'image': 'tesla_model_s_e_85d.jpg',
            'alt': 'Tesla Model S E 85D'
        }
    ]

    brand_logos = [
        'tesla_logo.png',
        'bmw_logo.png'
    ]

    return render_template('index.html', makes=makes, prices=prices, distances=distances, ads=ads, brand_logos=brand_logos)

@main.route('/vehicles', methods=['GET'])
def vehicles():
    make = request.args.get('make', 'any')
    model = request.args.get('model', 'any')
    year = request.args.get('year', 'any')
    from_year = request.args.get('from_year', 'any')
    to_year = request.args.get('to_year', 'any')
    mileage = request.args.get('mileage', 'any')
    top_speed = request.args.get('top_speed', 'any')
    acceleration = request.args.get('acceleration', 'any')
    min_price = request.args.get('min_price', 'any')
    max_price = request.args.get('max_price', 'any')
    color = request.args.get('color', 'any')

    query = Vehicle.query

    if make != 'any':
        query = query.filter_by(make=make)
    if model != 'any':
        query = query.filter_by(model=model)
    if from_year != 'any':
        query = query.filter(Vehicle.year >= int(from_year))
    if to_year != 'any':
        query = query.filter(Vehicle.year <= int(to_year))
    if year != 'any':
        query = query.filter(Vehicle.year == int(year))
    if mileage != 'any':
        query = query.filter(Vehicle.mileage <= int(mileage))
    if top_speed != 'any':
        query = query.filter(Vehicle.top_speed >= int(top_speed))
    if acceleration != 'any':
        query = query.filter(Vehicle.acceleration <= float(acceleration))
    if min_price != 'any':
        query = query.filter(Vehicle.price >= float(min_price))
    if max_price != 'any':
        query = query.filter(Vehicle.price <= float(max_price))
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
        from_year=from_year,
        to_year=to_year,
        mileage_value=mileage,
        top_speed_value=top_speed,
        acceleration_value=acceleration,
        min_price=min_price,
        max_price=max_price,
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