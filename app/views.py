from app import app
from flask import Flask, request, render_template
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
    shouldTerms = [{"term": {"ingredients": token}} for token in tokens]
    res = es.search (index="recipe", body={"query": {"bool": {"should": shouldTerms}}})
    data = res["hits"]["hits"]
    start_index = (page - 1) * 10
    end_index = start_index + 10
    paginated_data = data[start_index:end_index]

    # include the percent of ingredients matching in the data
    for i, result in enumerate(paginated_data):
        count = np.sum([1 if tokens.count(ingredient) > 0 else 0 for ingredient in  result["_source"]["ingredients"]])
        paginated_data[i] = (result, np.round(count * 100 / len(result["_source"]["ingredients"]), 2))
    
    return render_template('results.html', data=paginated_data, ingredients=tokens, page=page)

# TODO: Delete this when you have better instructions
# STEPS:
# 1. start elasticsearch cluster
# 2. run bonsai_load (remember to check the config for the correct elastic password, and copy the http_Ca cert)
# 2. run app.py, start developnig on views.py