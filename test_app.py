import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Vehicle, Brand, Model
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up the testing environment
        os.environ['FLASK_ENV'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        # Create sample user
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)

        # Create sample brand and model
        brand = Brand(name='Tesla')
        db.session.add(brand)
        db.session.commit()

        model1 = Model(name='Model 3', brand_id=brand.id)
        model2 = Model(name='Model S', brand_id=brand.id)
        db.session.add(model1)
        db.session.add(model2)
        db.session.commit()

        # Create sample vehicle records
        vehicle1 = Vehicle(brand=brand, model_rel=model1, year=2022, price=50000, color='Red', seller=user)
        vehicle2 = Vehicle(brand=brand, model_rel=model2, year=2021, price=80000, color='Blue', seller=user)
        db.session.add(vehicle1)
        db.session.add(vehicle2)

        db.session.commit()

    def tearDown(self):
        # Tear down the testing environment
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        # Test if the application instance exists
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        # Test if the application is in testing mode
        self.assertTrue(current_app.config['TESTING'])

    def test_index_route(self):
        # Test the index route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tesla Model 3', response.data)  # Ensure that the expected data is present
        print(response.data)  # Debugging line to print the response content

    def test_login_route(self):
        # Test the login route
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email', response.data)

    def test_signup_route(self):
        # Test the signup route
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username', response.data)

    def test_search_vehicles(self):
        # Test the vehicle search functionality
        with self.app.app_context():
            if Vehicle.query.count() == 0:
                self.skipTest("Skipping test because the database is empty")
            response = self.client.get('/search_results', query_string={
                'make': '1',
                'model': '1',
                'year': 2022,
                'price': 50000,
                'color': 'Red'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Tesla Model 3', response.data)  # Adjust based on actual data expected

    def test_user_signup(self):
        # Test the user signup functionality
        response = self.client.post('/signup', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        user = User.query.filter_by(email='newuser@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'newuser')

    def test_user_login(self):
        # Test the user login functionality
        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

if __name__ == '__main__':
    unittest.main()
