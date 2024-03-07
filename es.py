from elasticsearch import Elasticsearch, helpers
import numpy as np
import config
# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", config.elastic_password))

def isValidString(text):
    print([text])
    if text != None: return True
    return False

def handleInput():
    while True:
        print("Input your desired keyword")
        desiredKeyword = input()
        if isValidString(desiredKeyword): return desiredKeyword
        print("Invalid input. Please try again")

def handleMustQuery(columnName):
    cont = True
    mustTerms = list()
    while(cont):
        desiredKeyword = handleInput()
        mustTerms.append({"term": {columnName: desiredKeyword}})
        print("enter 0 to send query or 1 to continue adding terms")
        i = int(input())
        if i == 0: cont = False

    query = {"bool": {
                    "must":mustTerms}}
    
    return query

def handleShouldQuery(columnName):
    cont = True
    mustTerms = list()
    while(cont):
        desiredKeyword = handleInput()
        mustTerms.append({"term": {columnName: desiredKeyword}})
        print("enter 0 to send query or 1 to continue adding terms")
        i = int(input())
        if i == 0: cont = False

    query = {"bool": {"should":mustTerms}}
    
    return query

def showRecipes(docsList):
    while docsList:
        print("-----Recipe List-----")
        for index, doc in enumerate (docsList):
            recipe = doc["_source"]
            name = recipe["name"]
            print("{}. {}".format(index + 1, name))
        print("If you would like to see more details of a recipe listed, enter the number that was listed next to it. If you want to exit, enter 0.")
        i = input()
        if int(i) < 0 or int(i) > len(docsList): print("Invalid input. Please try again.")
        elif int(i) == 0: break
        else:
            print(docsList[int(i)-1]["_source"])

def getTopTen(docsList):
    page = 0
    while True:
        print("-----Recipe List-----")
        print("Page {}".format(page + 1))
        for i in range(np.min([len(docsList) - page*10, 10])):
            doc = docsList[page*10 + i]
            recipe = doc["_source"]
            name = recipe["name"]
            print("{}. {}".format(page*10 + i + 1, name))
        print("If you would like to see more details of a recipe listed, enter the number that was listed next to it. If you want to exit, enter 0. If you want to see the next page of results, press -1")
        i = input()
        if int(i) > len(docsList): print("Invalid input. Please try again.")
        elif int(i) == 0: break
        elif int(i) < 0: page += 1
        else:
            print(docsList[int(i)-1]["_source"])

def sendSearch(query):
    res = es.search (index="recipe", body={"query":query})
    numHits = len(res["hits"]["hits"])
    print(res)
    print("Num hits: {}".format(numHits))
    if numHits > 0: getTopTen(res["hits"]["hits"])
    
def main():
    while(True):
        print("Welcome to our recipe searcher! Select the option you'd like to use for your search.\n"
            "0. Exit\n1. Ingredients\n2. Recipe Name")
        i = int(input())
        query = None
        match i:
            case 0: break
            case 1: query = handleMustQuery("ingredients")
            case 2: query = handleMustQuery("name")
            case _: 
                print("Invalid number. Please try again.")
                break
        if query != None: sendSearch(query)
    print("Thank you!")


#This is an OR search
print("---OR SEARCH---")
query = handleShouldQuery("ingredients")
sendSearch(query)

# This is an AND search
#print("---AND SEARCH---")
#query = handleMustQuery("ingredients")
#sendSearch(query)