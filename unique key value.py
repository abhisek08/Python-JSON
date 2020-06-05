'''
Write a Python program to access only unique key value of a Python object.
'''
import json
j1='{"1":1,"1":2,"3":3,"4":4}'
p1=json.loads(j1)
print(p1)