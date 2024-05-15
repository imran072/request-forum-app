from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

def create_admin_user():
    admin_username = 'admin'
    admin_email = 'admin@example.com'
    admin_password = 'adminpassword'

    if not User.query.filter_by(username=admin_username).first():
        admin_user = User(username=admin_username, email=admin_email, is_admin=True)
        admin_user.set_password(admin_password)
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin user '{admin_username}' created successfully.")
    else:
        print(f"Admin user '{admin_username}' already exists.")

if __name__ == '__main__':
    create_admin_user()
