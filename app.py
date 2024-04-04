from app import app, db
from elasticsearch import Elasticsearch
import config

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))
cluster_info = es.info()
print(f"Connected to ElasticSearch cluster `{cluster_info['cluster_name']}`")
# {es.info().body['cluster_name']}cluster_info = es.info()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Run this to copy the http_Ca cert from docker elastic search container.
# docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .