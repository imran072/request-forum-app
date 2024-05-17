from . import db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import SignupForm, LoginForm, ResetPasswordForm, RequestResetForm
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from app import mail



auth = Blueprint('auth', __name__)

def send_reset_email(user):
    token = get_reset_token(user.email)
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth.reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

def get_reset_token(email, expires_sec=1800):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='password-reset-salt')



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
            flash(f'Hello, {user.username}! You have successfully logged in.', 'success') # category success
            login_user(user, remember=True) # Log the user in
            return redirect(url_for('main.index'))  # Redirect to the index page
        else:
            flash('Invalid email or password.', 'error')
    return render_template('login.html', form=form)

@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)
    except (SignatureExpired, BadSignature):
        flash('The reset link is invalid or has expired.', 'error')
        return redirect(url_for('auth.forgot_password'))
    
    form = ResetPasswordForm()
    user = User.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if user:
            user.set_password(form.password.data)
            db.session.commit()
            flash('Your password has been updated.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('No account found with that email.', 'warning')
            return redirect(url_for('auth.forgot_password'))
    else:
        # Add a debug statement here
        print("Form did not validate.")
    return render_template('reset_password.html', form=form, token=token)


@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = RequestResetForm()  # This will be a simple form with just an email field
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)  # Function to send an email
            flash('An email has been sent with instructions to reset your password.', 'info')
            return redirect(url_for('auth.login'))
        else:
            flash('No account found with that email.', 'warning')
    return render_template('forgot_password.html', form=form)



@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

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

