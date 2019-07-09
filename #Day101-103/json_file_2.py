import json 
array = '{"fruits": ["apple", "banana", "orange"]}'

data = json.loads(array)
data['fruits']
