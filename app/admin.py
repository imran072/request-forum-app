from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from . import db
from .models import Note, User, Offer, Vehicle, Brand, Model, VehicleAttributes, UserWatchlist, SearchHistory, Message

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect(url_for('auth.login'))
        return super(MyAdminIndexView, self).index()

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

def create_admin(app):
    from flask_admin import Admin
    admin = Admin(app, index_view=MyAdminIndexView())

    # Add model views
    admin.add_view(MyModelView(Note, db.session))
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Offer, db.session))
    admin.add_view(MyModelView(Vehicle, db.session))
    admin.add_view(MyModelView(Brand, db.session))
    admin.add_view(MyModelView(Model, db.session))
    admin.add_view(MyModelView(VehicleAttributes, db.session))
    admin.add_view(MyModelView(UserWatchlist, db.session))
    admin.add_view(MyModelView(SearchHistory, db.session))
    admin.add_view(MyModelView(Message, db.session))

    return admin
