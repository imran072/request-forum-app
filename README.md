# Request Forum APP / EV Marketplace

This is a web application that serves as a request forum, allowing users to create accounts, post their own requests, and answer other people's requests. The application aims to provide an engaging, effective, and intuitive platform for users to interact and exchange requests within a specific context or community.

## Features

- Search Function: Users can search for their ideal car with various filters provided.
- Built-in Message Communication: Sellers and buyers can communicate with each other within the web application.
- Make-an-offer: The buyer can offer a price to make the experience smooth and efficient.
- User Authentication: Users can register, log in, and reset their passwords.
- Listing Management: Users can create, edit, and delete vehicle listings.
- Profile: User has own account profile with all relevant information in it
- Admin Dashboard: Provides maintenance tools for a User with admin rights. 

## Technologies Used

- HTML, CSS
- Flask (Python web framework)
- AJAX, jQuery
- Bootstrap (CSS framework)
- SQLite (database)


## Launching the Application

### Prerequisites

Ensure you have Python 3.x installed on your system. It's recommended to use a virtual environment to manage dependencies.

1. Clone the repository:

   ```bash
   git clone https://github.com/imran072/request-forum-app.git
   cd request-forum-app
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. SKIP THIS STEP IF YOU ARE USING LMS version of the project: 
Set up environment variables:

   Create a `.env` file in the root directory and add necessary environment variables:

   ```ini
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   SQLALCHEMY_DATABASE_URI=sqlite:///marketplace.db

   ```

5. SKIP THIS STEP IF YOU HAVE A DUMMY DATABASE (LMS version HAS a dummy DB): 
Initialize the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   python populate_db.py
   ```

6. Run the application:

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Running Tests

To run the tests for your Flask application, follow these steps:

## Running Tests

To run the tests for your Flask application, follow these steps:

1. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Run the tests:
    - Assumption: Chromedriver for Selenium is installed and is in $PATH

    ```bash
    python3 -m unittest test_app.py 
    python3 test_selenium.py
    ```

By following these steps, you should be able to set up the environment, run the Flask application, and execute the tests successfully.

## File Structure

- `run.py`: Entry point for the application.
- `config.py`: Configuration file for the application.
- `populate_db.py`: Script to populate the database with initial data.
- `create_admin.py`: Script to create an admin user.
- `requirements.txt`: List of dependencies.
- `test_app.py`: Test cases for the application.
- `test_selenium.py`: Selenium tests for the application.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files (CSS, JS, images).

## Dependencies

The application uses the following key dependencies:

- alembic==1.13.1
- blinker==1.8.1
- click==8.1.7
- dnspython==2.6.1
- email_validator==2.1.1
- Flask==3.0.3
- Flask-Admin==1.6.1
- Flask-Login==0.6.3
- Flask-Mail==0.9.1
- Flask-Migrate==4.0.7
- Flask-SQLAlchemy==3.1.1
- Flask-Testing==0.8.1
- Flask-WTF==1.2.1
- idna==3.7
- itsdangerous==2.2.0
- Jinja2==3.1.3
- Mako==1.3.3
- MarkupSafe==2.1.5
- python-dotenv==1.0.1
- SQLAlchemy==2.0.29
- typing_extensions==4.11.0
- Werkzeug==3.0.2
- WTForms==3.1.2
- selenium==4.1.0
- webdriver-manager

For a full list of dependencies, refer to `requirements.txt`.


## Contributors

| UWA ID   | Name                  | GitHub Username |
|-----------|------------------------|-----------------|
| 23846485 | Kazi Imran            | imran072        |
| 23733728 | Zhanerken Azimbayev   | zhanerken       |
| 23985879 | Scarlett Peng         | jialipeng8      |
| 23827824 | Phoebus Lee           | pbuslee         |

## Reference 
AI Tools such as ChatGPT 4 and CodePilot were used in the development of this project
