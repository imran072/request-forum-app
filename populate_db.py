from app import create_app, db
from app.models import User, Vehicle, Brand, Model

def add_dummy_data():
    # Create dummy users if they don't already exist
    user1 = User.query.filter_by(username='john_doe').first()
    if not user1:
        user1 = User(username='john_doe', email='john@example.com')
        user1.set_password('test1234')
        db.session.add(user1)

    user2 = User.query.filter_by(username='jane_doe').first()
    if not user2:
        user2 = User(username='jane_doe', email='jane@example.com')
        user2.set_password('test1234')
        db.session.add(user2)

    # Commit the users to get their IDs
    db.session.commit()

    # Example data for brands and models
    brands_models = {
        'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y'],
        'Toyota': ['Camry', 'Corolla', 'Prius', 'RAV4'],
        'Ford': ['F-150', 'Mustang', 'Explorer', 'Escape']
    }

    # Populate the database with brands and models if they don't already exist
    for brand_name, models in brands_models.items():
        brand = Brand.query.filter_by(name=brand_name).first()
        if not brand:
            brand = Brand(name=brand_name)
            db.session.add(brand)
            db.session.commit()  # Save the brand to get the brand id

        for model_name in models:
            model = Model.query.filter_by(name=model_name, brand_id=brand.id).first()
            if not model:
                model = Model(name=model_name, brand_id=brand.id)
                db.session.add(model)

    db.session.commit()

    # Create dummy vehicles if they don't already exist
    vehicle1 = Vehicle.query.filter_by(make='Tesla', model='Model S', year=2020, seller_id=user1.id).first()
    if not vehicle1:
        vehicle1 = Vehicle(make='Tesla', model='Model S', year=2020, mileage=15000, battery_capacity=85,
                           color='Red', price=75000.00, doors=4, car_type='Sedan', top_speed=250,
                           acceleration=3.2, seller_id=user1.id)
        db.session.add(vehicle1)

    vehicle2 = Vehicle.query.filter_by(make='Nissan', model='Leaf', year=2018, seller_id=user2.id).first()
    if not vehicle2:
        vehicle2 = Vehicle(make='Nissan', model='Leaf', year=2018, mileage=30000, battery_capacity=40,
                           color='Blue', price=20000.00, doors=4, car_type='Hatchback', top_speed=150,
                           acceleration=7.9, seller_id=user2.id)
        db.session.add(vehicle2)

    # Commit the changes to the database
    db.session.commit()

    print('Database populated with dummy data!')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        add_dummy_data()
