'''
Write a Python program to convert JSON encoded data into Python objects.
'''
import json
j1='[0,1,2,3,4]'
j2='"True"'
j3='"abhisek"'
j4='13.56'
j5='{"a":1,"b":2}'
p1=json.loads(j1)
p2=json.loads(j2)
p3=json.loads(j3)
p4=json.loads(j4)
p5=json.loads(j5)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)