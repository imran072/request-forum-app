from . import db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import SignupForm, LoginForm, ResetPasswordForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            # Log the user in by setting session variables
            session['user_id'] = user.id
            session['username'] = user.username
            flash('You have successfully logged in.', 'success') # category success
            login_user(user, remember=True) # Log the user in
            return redirect(url_for('main.index'))  # Redirect to the index page
        else:
            flash('Invalid email or password.', 'error')
    return render_template('login.html', form=form)

@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user.set_password(form.password.data)
            db.session.commit()
            flash('Your password has been updated.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('No account found with that email.', 'warning')
    return render_template('reset_password.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if not existing_user:
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data)
            )
            db.session.add(new_user)
            db.session.commit()
            flash('You have successfully registered!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Email already exists.', 'error')
    return render_template('signup.html', form=form)

