import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app import create_app, db
from app.models import User
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.client = self.app.test_client()

        # Create a user
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        
        # Retrieve and validate user creation
        test_user = User.query.filter_by(email='test@example.com').first()
        if not test_user:
            raise Exception("Test user was not created.")
        if not test_user.check_password('password123'):
            raise Exception("Password for the test user is incorrect.")
        assert test_user.username == 'testuser', "Username does not match."

    def tearDown(self):
        # Cleanup code that runs after each test method
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        test_user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(test_user, "Test user was not created.")
        self.assertTrue(test_user.check_password('password123'), "Password for the test user is incorrect.")
        self.assertEqual(test_user.username, 'testuser', "Username does not match.")
        print(f"Username of the created test user: {test_user.username}")
        print(f"email of the created test user: {test_user.email}")
        
    def test_login(self):
        test_user = User.query.filter_by(email='test@example.com').first()
        self.driver.implicitly_wait(5)
        # Example test for login
        #wait = WebDriverWait(self.driver, 10)
        self.driver.get('http://127.0.0.1:5000/login') 
        
        # Enter email
        email_input = self.driver.find_element(By.ID, 'emailInput')  # Corrected to use the actual ID from your HTML
        email_input.send_keys('test@example.com')
        
        # Enter password
        password_input = self.driver.find_element(By.ID, 'passwordInput')  # Corrected to use the actual ID from your HTML
        password_input.send_keys('password123')
        
        # Submit form
        submit_button = self.driver.find_element(By.ID, 'login')
        submit_button.click()
        
        success_message = self.driver.find_element(By.ID, 'flashed_msg').text
        expected_message = f'Hello, testuser! You have successfully logged in.'
        self.assertIn(expected_message, success_message)


if __name__ == '__main__':
    unittest.main()
    
