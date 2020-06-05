'''
Write a Python program to convert JSON data to Python object.
'''
import json
json_obj='{"Name":"Abhisek","Class":10,"Roll":511705}'
python_obj=json.loads(json_obj)
print(python_obj)
print(python_obj['Name'])