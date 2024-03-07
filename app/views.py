from app import app
from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
import config
import numpy as np

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))
cluster_info = es.info()
print(f"Connected to ElasticSearch cluster `{cluster_info['cluster_name']}`")
page = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    print(request)
    query = request.args["q"].lower()
    tokens = query.split('_')
    data = []
    for token in tokens:
        res = es.search (index="recipe", body={"query": {"match": {"ingredients": token}}})
        data.append(res["hits"]["hits"])
    return render_template('results.html', data=getTopTen(np.concatenate(data)), ingredients=tokens, page=page)

def getTopTen(docsList):
    return [ docsList[page*10 + i] for i in range(np.min([len(docsList) - page*10 - 1, 10]))]

# TODO: Delete this when you have better instructions
# STEPS:
# 1. start elasticsearch cluster
# 2. run bonsai_load (remember to check the config for the correct elastic password, and copy the http_Ca cert)
# 2. run app.py, start developnig on views.py