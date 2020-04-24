import json

common_notions_path = './common_notions.json'

with open(common_notions_path, 'r') as f:
    common_notions = json.load(f)

# print(common_notions['common_notions'][2]['text']['greek'])