# Request Forum APP / EV Marketplace

This is a web application that serves as a request forum, allowing users to create accounts, post their own requests, and answer other people's requests. The application aims to provide an engaging, effective, and intuitive platform for users to interact and exchange requests within a specific context or community.

## Features

- Search Function: Users can search for their ideal car with various filters provided.
- Built-in Message Communication: Sellers and buyers can communicate with each other within the web application.
- Make-an-offer: The buyer can offer a price to make the experience smooth and efficient.
- User Authentication: Users can register, log in, and reset their passwords.
- Listing Management: Users can create, edit, and delete vehicle listings.

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
   git clone <repository_url>
   cd ev-marketplace
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

4. Set up environment variables:

   Create a `.env` file in the root directory and add necessary environment variables:

   ```ini
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db
   ```

5. Initialize the database:

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

1. Set up the virtual environment:
    - Create and activate a virtual environment to isolate your dependencies.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install dependencies:
    - Install the required dependencies from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    - Populate the database using the provided scripts.

    ```bash
    python populate_db.py
    python create_admin.py
    ```

4. Run the Flask application:
    - Start your Flask application.

    ```bash
    python run.py
    ```

5. Run the tests:
    - Execute the tests using the appropriate test framework. Your files indicate the use of Selenium for integration tests and possibly pytest for unit tests.

    ```bash
    pytest test_app.py
    pytest test_selenium.py
    ```

### Additional Information

- Configuring the Database: Ensure your `config.py` file is set up correctly to point to your SQLite database or another database system you are using.
- Environment Variables: If your application requires specific environment variables, ensure they are set. You can use a `.env` file for this purpose.

### Example .env File

If your application uses environment variables, create a `.env` file in your project root:

```ini
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///dummy_car_listing.db
SECRET_KEY=your_secret_key
```

### Example Commands to Run All Steps

```bash
# 1. Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up the database
python populate_db.py
python create_admin.py

# 4. Run the Flask application
python run.py

# 5. Run the tests
pytest test_app.py
pytest test_selenium.py
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

- Flask
- Flask-Admin
- Flask-Login
- Flask-Mail
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-WTF

For a full list of dependencies, refer to `requirements.txt`.


## Contributors

| UWA ID   | Name                  | GitHub Username |
|-----------|------------------------|-----------------|
| 23846485 | Kazi Imran            | imran072        |
| 23733728 | Zhanerken Azimbayev   | zhanerken       |
| 23985879 | Scarlett Peng         | jialipeng8      |
| 23827824 | Phoebus Lee           | pbuslee         |
