from app import app
from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    query = request.args["q"].lower()
    tokens = query.split('_')
    for token in tokens:
        print(token)
    return render_template('results.html')

# TODO: Delete this when you have better instructions
# STEPS:
# 1. start elasticsearch cluster
# 2. run bonsai_load (remember to check the config for the correct elastic password, and copy the http_Ca cert)
# 2. run app.py, start developnig on views.py