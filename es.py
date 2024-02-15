from elasticsearch import Elasticsearch, helpers
import numpy as np
# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", "FWDZ0*ObFet0G4RlxY+4"))

def isValidString(text):
    if text != None: return True
    return False

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

def showRecipes(docsList):
    while docsList:
        print("-----Recipe List-----")
        for index, doc in enumerate (docsList):
            recipe = doc["_source"]
            name = recipe["name"]
            print("{}. {}".format(index + 1, name))
        print("If you would like to see more details of a recipe listed, enter the number that was listed next to it. If you want to exit, enter 0.")
        i = int(input())
        if i == 0: break
        if i < 1 or i > len(docsList): print("Invalid input. Please try again.")
        else:
            print(docsList[i-1]["_source"])


def sendSearch(query):
    res = es.search (index="recipe", body={"query":query})
    numHits = len(res["hits"]["hits"])
    print("Num hits: {}".format(numHits))
    if numHits > 0: showRecipes(res["hits"]["hits"])
    

while(True):
    print("Welcome to our recipe searcher! Select the option you'd like to use for your search.\n"
        "1. Exit\n2. Ingredients\n3. Recipe Name")
    i = int(input())
    query = None
    match i:
        case 1: break
        case 2: query = handleQuery("ingredients")
        case 3: query = handleQuery("name")
        case _: 
            print("Invalid number. Please try again.")
            break
    if query != None: sendSearch(query)
print("Thank you!")