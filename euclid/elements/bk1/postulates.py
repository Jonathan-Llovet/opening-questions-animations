import json

postulates_path = './postulates.json'

with open(postulates_path, 'r') as f:
    postulates = json.load(f)
