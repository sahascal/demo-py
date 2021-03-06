
import math
import random
# print built in math functions
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
print("container types in Py - set, list, tuple and dict")
print("The second member of list: " + lst[3])
print('**********-----------------------------------------------**********')
print("The first member of tuple: " + tpl[3])
print('**********-----------------------------------------------**********')
print("The first k-v pair in dictionary: " + dct['Fname'])
print('**********-----------------------------------------------**********')

# classes and objects
a = 30
b= 'apple'
print('*-----------------------------------------------------------------*')
print("default classes in Py and objects")
print(a, b)
print("Type of a and b:", type(a), type(b))
print('**********-----------------------------------------------**********')
print("Mem location of a and b:", id(a), id(b)) 
print('**********-----------------------------------------------**********')
print(isinstance(a, int), isinstance(b, str))
print('*-----------------------------------------------------------------*')

#bin, oct and hex
print('*-----------------------------------------------------------------*')
print("convert integer to bin, oct and hex")
print("Binary of int-2:",bin(2))
print("Oct of int-16:", oct(16))
print("Hex of int-16:", hex(16))
print('*-----------------------------------------------------------------*')

#random number operations using random module
random.seed()
print('*-----------------------------------------------------------------*')
print("random operations using random module in Py")
print(random.random())
print(random.random())
print(random.randint(10,50))
print('*-----------------------------------------------------------------*')