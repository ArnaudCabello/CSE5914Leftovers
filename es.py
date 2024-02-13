from elasticsearch import Elasticsearch, helpers
import numpy as np
# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", "FWDZ0*ObFet0G4RlxY+4"))



def isValidString(text):
    if text != None: return True
    return False

def isValidInt(text):
    if text > 3 or text < 1: return False
    return True

def handleInput():
    while True:
        print("Input your desired keyword")
        desiredKeyword = input()
        if isValidString(desiredKeyword): return desiredKeyword
        print("Invalid input. Please try again")

def handleQuery(columnName):
    desiredKeyword = handleInput()
    query = {"match": {columnName: {"query": desiredKeyword}}}
    return query

def sendSearch(query):
    res = es.search (index="recipe", body={"query":query})
    print("Num hits: {}".format(len(res["hits"]["hits"])))
    for doc in res["hits"]["hits"]:
        print(doc)

while(True):
    print("Welcome to our recipe searcher! Select the option you'd like to use for your search.\n"
        "1. Exit\n2. Keywords\n3. Recipe Name")
    i = int(input())

    if i == 1: break
    query = None
    if i == 2: query = handleQuery("Keywords")
    if i == 3: query = handleQuery("Name")
    sendSearch(query)
print("Thank you!")