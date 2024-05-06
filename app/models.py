from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    vehicles = db.relationship('Vehicle', backref='seller', lazy='dynamic')
    watchlist = db.relationship('UserWatchlist', back_populates='user')
    search_histories = db.relationship('SearchHistory', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    battery_capacity = db.Column(db.Integer)
    color = db.Column(db.String(20))
    price = db.Column(db.Float)
    doors = db.Column(db.Integer)
    car_type = db.Column(db.String(50))
    top_speed = db.Column(db.Integer)
    acceleration = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))

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

