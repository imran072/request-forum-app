from app import create_app, db
from app.models import User, Vehicle, VehicleAttributes, UserWatchlist, SearchHistory


def add_dummy_data():
    # Create dummy users
    user1 = User(username='john_doe', email='john@example.com')
    user1.set_password('test1234')

    user2 = User(username='jane_doe', email='jane@example.com')
    user2.set_password('test1234')

    # Add users to session
    db.session.add(user1)
    db.session.add(user2)

    # Create dummy vehicles
    vehicle1 = Vehicle(make='Tesla', model='Model S', year=2020, mileage=15000, battery_capacity=85,
                       color='Red', price=75000.00, doors=4, car_type='Sedan', top_speed=250,
                       acceleration=3.2, seller_id=user1.id)

    vehicle2 = Vehicle(make='Nissan', model='Leaf', year=2018, mileage=30000, battery_capacity=40,
                       color='Blue', price=20000.00, doors=4, car_type='Hatchback', top_speed=150,
                       acceleration=7.9, seller_id=user2.id)

    # Add vehicles to session
    db.session.add(vehicle1)
    db.session.add(vehicle2)

    # Commit the changes to the database
    db.session.commit()

    print('Database populated with dummy data!')


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        add_dummy_data()
