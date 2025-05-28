from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    search_term = request.args.get('search', '').strip()
    if search_term:
        query = f"%{search_term}%"
        stmt = db.select(Destination).where(Destination.description.like(query))
        destinations = db.session.scalars(stmt).all()  # Convert iterator to list
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))