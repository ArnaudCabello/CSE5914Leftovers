from app import app

from flask import render_template 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    return render_template('results.html')