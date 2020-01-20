"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from RedditPy import app
import json
import RedditPy.hwswap

searchterms = "What You're Tracking"
searchtermsobj = { "arr": ["570", "580"]}
tsearches = []
tsearches.append("570")

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
        sterms = searchterms,
        searches = tsearches
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.jade',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/addtolist', methods=['POST'])
def addSearchTerm():
    tsearches.append(request.form['searchterm'])
    RedditPy.hwswap.hwswapper(request.form['searchterm'])
    return redirect(url_for('home'))
