import json

definitions_path = './definitions.json'

with open(definitions_path, 'r') as f:
    definitions = json.load(f)

# print(definitions['definitions'][2]['text']['greek'])
