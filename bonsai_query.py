from elasticsearch import Elasticsearch, helpers
import config

# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))

# DELETE ALL RECIPES
# es.delete_by_query(index="recipe", body={"query": {"match_all": {}}})

res = es.search (index="recipe", body={"query": {"match": {"ingredients": "onion"}}})
print(len(res["hits"]["hits"]))
# for doc in res["hits"]["hits"]:
#   print(doc)
res = es.search (index="recipe", body={"query": {"match": {"ingredients": "water"}}})
print(len(res["hits"]["hits"]))
# for doc in res["hits"]["hits"]:
#   print(doc)

res = es.search (index="recipe", body={"query": {"match": {"ingredients": "onino"}}})
print(len(res["hits"]["hits"]))

res = es.search (index="recipe", body={"query": {"match": {"ingredients":{"query": "onino", "fuzziness": "AUTO"}}}})
print(len(res["hits"]["hits"]))


