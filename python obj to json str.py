'''
Write a Python program to convert Python objects into JSON strings. Print all the values.
'''
import json
p1={'name':'abhi','roll':2}
p2=['2','3']
p3=('1','12')
p4=True
p5=134.56
j1=json.dumps(p1)
j2=json.dumps(p2)
j3=json.dumps(p3)
j4=json.dumps(p4)
j5=json.dumps(p5)
print(j1)
print(j2)
print(j3)
print(j4)
print(j5)