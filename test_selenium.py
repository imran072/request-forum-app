import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app import create_app, db
from app.models import User
import os

class TestUserInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(executable_path="/Users/kazimdimran/Desktop/UWA/projects/request-forum-app/chromedriver")
        cls.driver = webdriver.Chrome(service=service)

    @classmethod
    def tearDownClass(cls):
        # Cleanup code that runs after all tests are done
        cls.driver.quit()

    def setUp(self):
        # Setup code that runs before each test method
        os.environ['FLASK_ENV'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a user
        user = User(username='selenium', email='selenium@example.com', password_hash='password')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        # Cleanup code that runs after each test method
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login(self):
        # Example test for login
        self.driver.get('http://127.0.0.1:5000/login')  # Update with your application's URL
        self.driver.find_element_by_name('email').send_keys('selenium@example.com')
        self.driver.find_element_by_name('password').send_keys('password')
        self.driver.find_element_by_id('submit').click()
        assert 'Welcome' in self.driver.page_source

if __name__ == '__main__':
    unittest.main()