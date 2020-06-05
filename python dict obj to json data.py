'''
Write a Python program to convert Python dictionary object (sort by key) to JSON data.
Print the object members with indent level 4.
'''
import json
p1={'a':1,'2':2,'3':3}
j1=json.dumps(p1,sort_keys=True,indent=10)
print(j1)