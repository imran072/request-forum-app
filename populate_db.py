from app import create_app, db
from app.models import User, Vehicle, Brand, Model

def add_dummy_data():
    try:
        # Create dummy users if they don't already exist
        user1 = User.query.filter_by(username='john_doe').first()
        if not user1:
            user1 = User(username='john_doe', email='john@example.com')
            user1.set_password('test1234')  # Ensure this method hashes the password
            db.session.add(user1)

        user2 = User.query.filter_by(username='jane_doe').first()
        if not user2:
            user2 = User(username='jane_doe', email='jane@example.com')
            user2.set_password('test1234')  # Ensure this method hashes the password
            db.session.add(user2)

        # Commit the users to get their IDs
        db.session.commit()

        # Example data for electric vehicle brands and models
        brands_models = {
            'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y', 'Cybertruck', 'Roadster'],
            'Nissan': ['Leaf', 'Ariya'],
            'Chevrolet': ['Bolt EV', 'Bolt EUV'],
            'BMW': ['i3', 'i4', 'iX', 'i8'],
            'Ford': ['Mustang Mach-E', 'F-150 Lightning'],
            'Hyundai': ['Kona Electric', 'Ioniq 5', 'Ioniq 6'],
            'Kia': ['Soul EV', 'EV6', 'Niro EV'],
            'Audi': ['e-tron', 'Q4 e-tron', 'e-tron GT'],
            'Volkswagen': ['ID.3', 'ID.4', 'ID. Buzz'],
            'Porsche': ['Taycan'],
            'Rivian': ['R1T', 'R1S'],
            'Lucid Motors': ['Air', 'Gravity'],
            'Polestar': ['Polestar 1', 'Polestar 2'],
            'Jaguar': ['I-PACE'],
            'Volvo': ['XC40 Recharge', 'C40 Recharge'],
            'Mercedes-Benz': ['EQC', 'EQS', 'EQB', 'EQE'],
            'Honda': ['Honda e'],
            'Mazda': ['MX-30'],
            'Mini': ['Mini Electric (Mini Cooper SE)'],
            'Subaru': ['Solterra'],
            'Toyota': ['bZ4X'],
            'Fisker': ['Ocean']
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

        print('Database populated with dummy data!')

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        add_dummy_data()
