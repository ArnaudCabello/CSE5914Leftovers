from app import app, dbmodels, db, login_manager
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from elasticsearch import Elasticsearch
import config
import numpy as np

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))
cluster_info = es.info()
print(f"Connected to ElasticSearch cluster `{cluster_info['cluster_name']}`")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    print(request)
    page = int(request.args.get("page", 1))
    query = request.args["q"].lower()
    tokens = query.split('_')
    data = []
    for token in tokens:
        res = es.search (index="recipe", body={"query": {"match": {"ingredients": token}}})
        data.extend(res["hits"]["hits"])
    start_index = (page - 1) * 10
    end_index = start_index + 10
    paginated_data = data[start_index:end_index]
    return render_template('results.html', data=paginated_data, ingredients=tokens, page=page)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing = dbmodels.User.query.filter_by(email=email).first()
        # If the user exists, prompt for another, otherwise create
        if existing:
            return "Username already exists"
        else: 
            new_user = dbmodels.User(email=email)
            new_user.set_hashed_password(password)
            db.session.add(new_user)
            db.session.commit()
            return "Registration successful"
        
    return render_template('register.html')

# used to keep user logged in during session
@login_manager.user_loader
def load_user(user_id):
    user = dbmodels.User.query.get(int(user_id))
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the database for the user based on email
        existing = dbmodels.User.query.filter_by(email=email).first()

        if existing and existing.check_password(password):
            # If the user exists and password matches, log in the user
            login_user(existing)
            return redirect(url_for('profile'))  # Redirect to the home page after successful login
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login')) # may want to change how this works later

    return render_template('login.html')

# will logout user and redirect to another page (currently login page)
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()  # Logout the user using Flask-Login
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('login'))  # Redirect to the login page after logout

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

def getTopTen(docsList):
    return [ docsList[page*10 + i] for i in range(np.min([len(docsList) - page*10 - 1, 10]))]

# TODO: Delete this when you have better instructions
# STEPS:
# 1. start elasticsearch cluster
# 2. run bonsai_load (remember to check the config for the correct elastic password, and copy the http_Ca cert)
# 2. run app.py, start developnig on views.py