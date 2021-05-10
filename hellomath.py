# print built in math functions
import math
import random

print(dir(__builtins__))
print('**********===============================================**********')
print(dir(math),sep='-')
print('**********===============================================**********')
# container types
lst = ['orange', 'banana', 'apple', 'grapes']
tpl = ('Sam', '44', 'BLR', 'WF')
st = {10,20,99,30,40}
dct = {'Fname':'Sam', 'Gender':'Male', 'Age': '33'}
print('**********-----------------------------------------------**********')
print("The second member of list: " + lst[3])
print('**********-----------------------------------------------**********')
print("The first member of tuple: " + tpl[3])
print('**********-----------------------------------------------**********')
print("The first k-v pair in dictionary: " + dct['Fname'])
print('**********-----------------------------------------------**********')
print('**********-----------------------------------------------**********')

a = 30
b= 'apple'
print(a, b)
print('**********-----------------------------------------------**********')
print("Type of a and b:" type(a), type(b))
print('**********-----------------------------------------------**********')
print("Mem location of a and b:", id(a), id(b)) 
print('**********-----------------------------------------------**********')