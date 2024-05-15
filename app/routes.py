from flask import Blueprint, render_template, request, url_for, flash, redirect, current_app, session
from .models import Vehicle, Brand, Model
from .forms import SearchForm, AddListingForm, MessageForm
from . import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from flask import jsonify
from app.models import User, Message
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    brands = Brand.query.all()
    vehicles = Vehicle.query.limit(10).all()  # Fetch the latest 10 vehicles for the ads
    return render_template('index.html', brands=brands, vehicles=vehicles)

@main.route('/search', methods=['GET', 'POST'])
def search_vehicles():
    form = MessageForm()  # Instantiate the MessageForm
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

        return render_template('search_results.html', vehicles=vehicles, form=form)

    brands = Brand.query.all()
    makes = [(brand.id, brand.name) for brand in brands]
    years = sorted(set(vehicle.year for vehicle in Vehicle.query.all()))
    mileages = sorted(set(vehicle.mileage for vehicle in Vehicle.query.all()))
    top_speeds = sorted(set(vehicle.top_speed for vehicle in Vehicle.query.all()))
    accelerations = sorted(set(vehicle.acceleration for vehicle in Vehicle.query.all()))
    prices = sorted(set(vehicle.price for vehicle in Vehicle.query.all()))
    colors = sorted(set(vehicle.color for vehicle in Vehicle.query.all()))

    return render_template('search.html', makes=makes, years=years, mileages=mileages, top_speeds=top_speeds, accelerations=accelerations, prices=prices, colors=colors)

@main.route('/messages', methods=['GET', 'POST'])
@login_required
def messages():
    form = MessageForm()
    if form.validate_on_submit():
        recipient = User.query.get(form.recipient.data)
        message = Message(sender_id=current_user.id, recipient_id=recipient.id, body=form.body.data)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent.', 'success')
        return redirect(url_for('main.messages'))
    sent_messages = Message.query.filter_by(sender_id=current_user.id).order_by(Message.timestamp.desc()).all()
    received_messages = Message.query.filter_by(recipient_id=current_user.id).order_by(Message.timestamp.desc()).all()
    return render_template('messages.html', form=form, sent_messages=sent_messages, received_messages=received_messages)

@main.route('/send_message', methods=['POST'])
@login_required
def send_message():
    form = MessageForm()
    if form.validate_on_submit():
        recipient = User.query.filter_by(username=form.recipient.data).first()
        if recipient:
            message = Message(sender_id=current_user.id, recipient_id=recipient.id, body=form.body.data)
            db.session.add(message)
            db.session.commit()
            flash('Your message has been sent.', 'success')
        else:
            flash('Recipient not found.', 'danger')
    else:
        flash('Failed to send message. Please check the form.', 'danger')
    return redirect(url_for('main.messages'))


@main.route('/search_results')
def search_results():
    vehicles = Vehicle.query.all()  # Replace with actual search query results
    form = MessageForm()  # Instantiate the MessageForm
    return render_template('search_results.html', vehicles=vehicles, form=form)

@main.route('/add_listing', methods=['GET', 'POST'])
@login_required
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
