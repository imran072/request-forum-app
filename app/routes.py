from flask import Blueprint, render_template, request, url_for, flash, redirect, current_app, session, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
import os

from .models import Vehicle, Brand, Model, User, Message
from .forms import SearchForm, AddListingForm, MessageForm, ReplyForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    brands = Brand.query.all()
    vehicles = Vehicle.query.order_by(Vehicle.timestamp.desc()).limit(10).all()  # Fetch the latest 10 vehicles sorted by timestamp
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


@main.route("/messages", methods=["GET", "POST"])
@login_required
def messages():
    form = MessageForm()
    reply_form = ReplyForm()
    if form.validate_on_submit():
        recipient = User.query.filter_by(username=form.recipient.data).first()
        if recipient:
            message = Message(author=current_user, recipient=recipient, body=form.body.data)
            db.session.add(message)
            db.session.commit()
            flash('Your message has been sent.', 'success')
        else:
            flash('User not found.', 'danger')

    sent_messages = current_user.sent_messages.order_by(Message.timestamp.desc()).all()
    received_messages = current_user.received_messages.order_by(Message.timestamp.desc()).all()
    return render_template("messages.html", form=form, sent_messages=sent_messages, received_messages=received_messages,
                           reply_form=reply_form)


@main.route("/reply_message", methods=["POST"])
@login_required
def reply_message():
    form = ReplyForm()
    if form.validate_on_submit():
        recipient = User.query.filter_by(username=form.recipient.data).first()
        if recipient:
            message = Message(author=current_user, recipient=recipient, body=form.body.data)
            db.session.add(message)
            db.session.commit()
            flash('Your reply has been sent.', 'success')
        else:
            flash('User not found.', 'danger')

    sent_messages = current_user.sent_messages.order_by(Message.timestamp.desc()).all()
    received_messages = current_user.received_messages.order_by(Message.timestamp.desc()).all()
    return render_template("messages.html", form=MessageForm(), sent_messages=sent_messages,
                           received_messages=received_messages, reply_form=form)


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
    form = SearchForm()
    make = request.args.get('make')
    model = request.args.get('model')
    price = request.args.get('price')

    query = Vehicle.query

    if make and make != 'any':
        query = query.filter_by(make=make)
    if model and model != 'any':
        query = query.filter_by(model=model)
    if price and price != 'any':
        query = query.filter(Vehicle.price <= int(price))

    vehicles = query.all()

    return render_template('search_results.html', vehicles=vehicles, form=form)

@main.route('/add_listing', methods=['GET', 'POST'])
@login_required
def add_listing():
    form = AddListingForm()

    # Populate brand choices
    brands = [(brand.id, brand.name) for brand in Brand.query.all()]
    form.make.choices = [(0, 'Select a brand')] + brands

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

@main.route('/get_brands')
def get_brands():
    brands = Brand.query.all()  # Adjust this line based on how you fetch brands
    return jsonify([{'id': brand.id, 'name': brand.name} for brand in brands])

@main.route('/get_models/<int:brand_id>')
def get_models(brand_id):
    models = Model.query.filter_by(brand_id=brand_id).all()  # Adjust this line based on your model fetching logic
    return jsonify([{'id': model.id, 'name': model.name} for model in models])

@main.route('/profile')
@login_required
def profile():
    user_id = current_user.id
    user = User.query.get(user_id)
    listings = Vehicle.query.filter_by(seller_id=user_id).all()
    return render_template('profile.html', user=user, listings=listings)

@main.route('/edit_listing/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_listing(id):
    vehicle = Vehicle.query.get_or_404(id)
    form = AddListingForm(obj=vehicle)

    # Populate 'make' choices on every request
    form.make.choices = [(brand.id, brand.name) for brand in Brand.query.order_by('name').all()]
    #print(form.make.choices)

    if request.method == 'POST':
        # Update model choices based on selected make
        form.model.choices = [(model.id, model.name) for model in Model.query.filter_by(brand_id=form.make.data).all()]

        if form.validate_on_submit():
            if form.image.data:
                image_file = form.image.data
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.root_path, 'static/img', filename)
                image_file.save(image_path)
                vehicle.image_url = url_for('static', filename='img/' + filename)
                
            form.populate_obj(vehicle)
            db.session.commit()
            flash('Listing updated successfully!', 'success')
            return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        # Populate make and model with existing data
        form.make.data = vehicle.make
        form.model.choices = [(model.id, model.name) for model in Model.query.filter_by(brand_id=vehicle.make).all()]
        form.model.data = vehicle.model

    return render_template('edit_listing.html', form=form, vehicle=vehicle)

@main.route('/delete_listing/<int:id>', methods=['POST'])
@login_required
def delete_listing(id):
    vehicle = Vehicle.query.get(id)
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, message="Vehicle not found"), 404

@main.route('/contactus')
def contactus():
    return render_template('contactus.html')