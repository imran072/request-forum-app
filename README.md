# Request Forum App - EV Marketplace

This project is an e-commerce platform for electric vehicles (EVs) where users can post car listings, make offers, accept offers, and communicate through messages. It includes functionalities like user authentication, adding listings, making and accepting offers, and more.

## Features

- **User Authentication**: Supports login, logout, and password reset functionalities.
- **Listings Management**: Users can add, edit, and delete their car listings.
- **Offer System**: Users can make offers on cars and accept or reject offers.
- **Messaging System**: A real-time chat feature for communication between buyers and sellers.
- **Search Functionality**: Users can search for car listings based on various filters.

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (Version control system)

### Clone the Repository

First, clone the repo from GitHub to your local machine:

```bash
git clone https://github.com/imran072/request-forum-app.git
cd request-forum-app

### Setup Virtual Environment

```bash
# For macOS and Linux:
python3 -m venv env
source env/bin/activate

# For Windows:
python -m venv env
.\\env\\Scripts\\activate

### Install Requisit Pacakages

`pip install -r requirements.txt`

### Configure .ENV

`touch mkdir .env`

FLASK_ENV=development
SECRET_KEY=your_secret_key_here
SQLALCHEMY_DATABASE_URI=sqlite:///marketplace.db
MAIL_USERNAME=noreply.evmarketplace@gmail.com
MAIL_PASSWORD=nzsvmhjtedysntbh

### Configure SQLite

```bash
flask db init
flask db migrate
flask db upgrade

### Populate DB With Dummy Data (Optional)

`python3 populate_db.py`

### Run The App

`flask run`


## Contributors

| UWA ID   | Name                  | GitHub Username |
|-----------|------------------------|-----------------|
| 23846485 | Kazi Imran            | imran072        |
| 23733728 | Zhanerken Azimbayev   | zhanerken       |
| 23985879 | Scarlett Peng         | jialipeng8      |
| 23827824 | Phoebus Lee           | pbuslee         |
