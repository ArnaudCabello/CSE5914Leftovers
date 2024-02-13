from elasticsearch import Elasticsearch

import csv

def cleanList(string):
    newString = string.replace("{", "[")
    newString = newString.replace("}", "]")
    newString = newString.replace("['", "[\"")
    strToReplace = ["','", "\",'", "',\"", "' ,'", "\" ,'", "' ,\"", "', '", "\", '", "', \"", "' , '", "\" , '", "' , \""]
    newString = newString.replace("']", "\"]")
    for str in strToReplace:
        newString = newString.replace(str, "\",\"")
    return newString

with open("test.csv", "r") as i:
    rows = rows = len(list(csv.reader(i)))

lineStr = "["
with open("recipes.json", "w") as o:
    with open("test.csv", "r") as i:
        reader = csv.reader(i)
        # data = list(reader)
        # rows = len(data)

        for i, line in enumerate(reader):
            lineStr += "{\"_op_type\": \"index\", \"_index\": \"recipe\","
            lineStr += "\"id\":" + line[0] + ","
            lineStr += "\"name\":\"" + line[1] + "\","
            lineStr += "\"ingredients\":" + cleanList(line[3]) + ","
            lineStr += "\"ingredients_raw_str\":" + cleanList(line[4]) + ","
            lineStr += "\"serving_size\":\"" + line[5] + "\","
            lineStr += "\"servings\":\"" + line[6] + "\","
            lineStr += "\"steps\":" + cleanList(line[7]) + ","
            lineStr += "\"tags\":" + cleanList(line[8]) + ","
            termsStr = line[9]
            lineStr += "\"search_terms\":" + cleanList(termsStr)
            if(reader.line_num == rows):
                lineStr += "}]"
            else:
                lineStr += "},\n"
            o.write(lineStr)
            lineStr = ""

