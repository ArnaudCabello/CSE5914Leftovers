from elasticsearch import Elasticsearch, helpers

# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(es_header)

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", "FWDZ0*ObFet0G4RlxY+4"))

def validString(text):
    if(text != None): return True
    return False

def handleKeywords():
    desiredKeyword = None
    print("Input your desired keyword")
    desiredKeyword = input()
    if not validString(desiredKeyword): return
    query = {"match": {"Keywords": desiredKeyword}}
    return query

def sendSearch(query):
    res = es.search (index="recipe", body={"query":query})
    print("Num hits: {}".format(len(res["hits"]["hits"])))
    for doc in res["hits"]["hits"]:
        print(doc)

while(True):
    print("Welcome to our recipe searcher! Select the option you'd like to use for your search.\n"
        "1. Exit\n2. Keywords")
    i = int(input())
    if i == 1: break
    query = None
    if i == 2: query = handleKeywords()
    sendSearch(query)
print("Thank you!")