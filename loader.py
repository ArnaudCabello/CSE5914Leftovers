from elasticsearch import Elasticsearch

import csv
import json
import ast

# Input and output file to use
input_file = "recipes_w_search_terms.csv"
output_file = "recipes.json"

with open(input_file, "r") as input:
        rows = len(input.readlines())

lineStr = "["
with open(output_file, "w") as output:
    with open(input_file, "r") as input:
        reader = csv.reader(input)
        output.write("[")
        # Create json line by line and output to json file
        for i, line in enumerate(reader):
            line9 = line[9].replace("{", "[")
            line9 = line9.replace("}", "]")
            json_line = {
                "_op_type": "index",
                "_index": "recipe",
                "id": line[0],
                "name": line[1],
                "description": line[2],
                "ingredients": ast.literal_eval(line[3]),
                "ingredients_raw_str": ast.literal_eval(line[4]),
                "serving_size": line[5],
                "servings": line[6],
                "steps": ast.literal_eval(line[7]),
                "tags": ast.literal_eval(line[8]),
                "search_terms": ast.literal_eval(line9)
            }
            output.write(json.dumps(json_line))
            if(reader.line_num == rows):
                output.write("]")
            else:
                output.write(",\n")
            print("Converted recipe id " + line[0])
