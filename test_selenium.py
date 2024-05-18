import unittest
from flask import Flask
from multiprocessing import Process
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from app import create_app, db
from app.models import User

def run_server():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    try:
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(f"Error setting up database: {e}")
    app.run(debug=False, use_reloader=False, port=5000)

class TestUserInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = Process(target=run_server)
        cls.server_process.start()
        print("Server started")
        service = Service(executable_path="/Users/kazimdimran/Desktop/UWA/projects/request-forum-app/chromedriver")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.server_process.terminate()
        cls.server_process.join()
        print("Server stopped")

    def test_login(self):
        self.driver.get('http://127.0.0.1:5000/login')
        email_input = self.driver.find_element(By.ID, 'emailInput')
        email_input.send_keys('test@example.com')
        password_input = self.driver.find_element(By.ID, 'passwordInput')
        password_input.send_keys('password123')
        submit_button = self.driver.find_element(By.ID, 'login')
        submit_button.click()
        success_message = self.driver.find_element(By.ID, 'flashed_msg').text
        self.assertIn('Hello, testuser! You have successfully logged in.', success_message)

if __name__ == '__main__':
    unittest.main()
