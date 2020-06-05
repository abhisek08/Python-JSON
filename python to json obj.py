'''
Write a Python program to convert Python object to JSON data.
'''
import json
python_obj={"Name":"Abhisek","Class":10,"Roll":511705}
json_obj= json.dumps(python_obj)
print(json_obj)
print(json_obj[1:-1])