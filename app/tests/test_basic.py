import unittest
from flask_testing import TestCase
from app import create_app, db
from config import TestingConfig

class TestBase(TestCase):
    def create_app(self):
        # Initialize the app with the TestingConfig
        app = create_app(config_class=TestingConfig)
        return app

    def setUp(self):
        # Create all tables
        db.create_all()

        # You can add other setup actions here, like inserting initial test data

    def tearDown(self):
        # Drop all tables and clean up the DB
        db.session.remove()
        db.drop_all()

# Example test case to demonstrate testing a route
class TestRoutes(TestBase):
    def test_home_route(self):
        # Send a request to the Flask app to the home route
        response = self.client.get('/')
        # Check if the response is valid
        self.assertEqual(response.status_code, 200)
        # You can add more assertions here to validate the response data, headers, etc.

# Run the tests
if __name__ == '__main__':
    unittest.main()
