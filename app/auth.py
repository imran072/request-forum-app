from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p> Login</p>"

@auth.route('/logout')
def logout():
    return "<p> Logout</p>"

@auth.route('/signup')
def signup():
    return "<p> Signup </p>"