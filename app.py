from app import app
from elasticsearch import Elasticsearch
import config

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))
cluster_info = es.info()
print(f"Connected to ElasticSearch cluster `{cluster_info['cluster_name']}`")
# {es.info().body['cluster_name']}cluster_info = es.info()
if __name__ == "__main__":
    app.run(debug=True)

    