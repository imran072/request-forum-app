import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Vehicle
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TestApp(unittest.TestCase):
    def setUp(self):
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

        # Create sample vehicle records
        vehicle1 = Vehicle(make='Tesla', model='Model 3', year=2022, price=50000, color='Red', seller=user)
        vehicle2 = Vehicle(make='Tesla', model='Model S', year=2021, price=80000, color='Blue', seller=user)
        db.session.add(vehicle1)
        db.session.add(vehicle2)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tesla Model 3', response.data)

    def test_login_route(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email', response.data)

    def test_signup_route(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username', response.data)

    def test_search_vehicles(self):
        with self.app.app_context():
            if Vehicle.query.count() == 0:
                self.skipTest("Skipping test because the database is empty")
            response = self.client.post('/search_vehicles', data={
                'make': 'Tesla',
                'model': 'Model 3',
                'year': 2022,
                'price': 50000,
                'color': 'Red'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Tesla', response.data)
            self.assertIn(b'Model 3', response.data)

    def test_user_signup(self):
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
        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

if __name__ == '__main__':
    unittest.main()