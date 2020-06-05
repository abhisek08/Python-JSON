'''
Write a Python program to create a new JSON file from an existing JSON file
'''
import json
f1=open('j.json',mode='w')
dict='{"a":1,"b":2}'
f1.write(dict)
f1.close()
print(f1)
dict1='{"c":1,"d":2}'
f1=json.dumps(dict1)
print(f1)
f1=open('j.json',mode='w')
f1.write(dict1)
f1.close()