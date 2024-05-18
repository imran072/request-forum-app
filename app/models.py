from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime, index=True, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<User {self.username}>'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=func.now())
    notes = db.relationship('Note', backref='user', lazy='dynamic')
    watchlist = db.relationship('UserWatchlist', back_populates='user', lazy='dynamic')
    vehicles = db.relationship('Vehicle', backref='seller', lazy='dynamic')
    is_admin = db.Column(db.Boolean, default=False)
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='author', lazy='dynamic')
    received_messages = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')
    offers_sent = db.relationship('Offer', foreign_keys='Offer.sender_id', backref='sender', lazy=True)
    offers_received = db.relationship('Offer', foreign_keys='Offer.recipient_id', backref='recipient', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id', name='fk_offer_vehicle_id', ondelete='CASCADE'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_offer_sender_id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_offer_recipient_id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default='Pending')  # 'Pending', 'Accepted', 'Rejected'
    vehicle = db.relationship('Vehicle', backref='offers')

    def __repr__(self):
        return f'<Offer {self.amount} from {self.sender_id} to {self.recipient_id}>'


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.Integer, db.ForeignKey('brand.id'))
    model = db.Column(db.Integer, db.ForeignKey('model.id'))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    battery_capacity = db.Column(db.Integer)
    color = db.Column(db.String(20))
    price = db.Column(db.Float)
    doors = db.Column(db.Integer)
    car_type = db.Column(db.String(50))
    top_speed = db.Column(db.Integer)
    acceleration = db.Column(db.Float)
    image_url = db.Column(db.String(255))
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    brand = db.relationship('Brand', backref='vehicles')
    model_rel = db.relationship('Model', backref='vehicles')

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    models = db.relationship('Model', backref='brand', lazy=True)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)

class VehicleAttributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    attribute_name = db.Column(db.String(50))
    attribute_value = db.Column(db.String(100))

class UserWatchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user = db.relationship('User', back_populates='watchlist')
    vehicle = db.relationship('Vehicle', backref=db.backref('watchlisted_by', lazy='dynamic'))

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    search_parameters = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.body}>'
