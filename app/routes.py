from flask import Blueprint, render_template
from flask import render_template, request
from .models import Vehicle
from .forms import SearchForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = Vehicle.query
        if form.make.data:
            query = query.filter(Vehicle.make.like('%' + form.make.data + '%'))
        if form.model.data:
            query = query.filter(Vehicle.model.like('%' + form.model.data + '%'))
        if form.min_price.data:
            query = query.filter(Vehicle.price >= form.min_price.data)
        if form.max_price.data:
            query = query.filter(Vehicle.price <= form.max_price.data)

        results = query.all()
        return render_template('search_results.html', results=results, form=form)

    return render_template('search.html', form=form)
