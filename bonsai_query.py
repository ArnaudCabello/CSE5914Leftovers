from elasticsearch import Elasticsearch, helpers

# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", "FWDZ0*ObFet0G4RlxY+4"))

# DELETE ALL RECIPES
# es.delete_by_query(index="recipe", body={"query": {"match_all": {}}})

res = es.search (index="recipe", body={"query": {"match": {"RecipeIngredientParts": "blueberries"}}})
print(len(res["hits"]["hits"]))
for doc in res["hits"]["hits"]:
  print(doc)
res = es.search (index="recipe", body={"query": {"match": {"RecipeIngredientParts": "yogurt"}}})
print(len(res["hits"]["hits"]))
for doc in res["hits"]["hits"]:
  print(doc)

res = es.search (index="recipe", body={"query": {"match": {"RecipeIngredientParts": "yogrt"}}})
print(len(res["hits"]["hits"]))

res = es.search (index="recipe", body={"query": {"match": {"RecipeIngredientParts":{"query": "yogrt", "fuzziness": "AUTO"}}}})
print(len(res["hits"]["hits"]))


