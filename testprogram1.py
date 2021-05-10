#swap two variables without using arithmetic operations
import math
a=2
b="good"
print("| = = = = = = = = = = = = = = = = = = = |")
print("without using arithmetic operation")
print("before swap:")
print("a is:",a, "and b is:", b)
print("| = = = = = = = = = = = = = = = = = = = |")
a,b = b,a
print("after swap")
print("a is:",a, "and b is:", b)
print("| = = = = = = = = = = = = = = = = = = = |")
#using XOR operator
a=5; b=50
print("| = = = = = = = = = = = = = = = = = = = |")
print("using xor operation")
print("before swap")
print("a is:",a, "and b is:", b)
a=a^b; print("xor op-1 a:",a)
b=a^b; print("xor op-2 b:",b)
a=a^b; print("xor op-3 a:",a)
print("after swap")
print("a is:",a, "and b is:", b)
print("| = = = = = = = = = = = = = = = = = = = |")

#understand trunc, floor and ceil for numbers
a=-2.8
print("trunc of -2.8:",math.trunc(a)) 
print("floor of -2.8:",math.floor(a)) 
print("ceil of -2.8:",math.ceil(a))
b=1.5
print("\n")
print("trunc of 1.5:",math.trunc(b)) 
print("floor of 1.5:",math.floor(b)) 
print("ceil of 1.5:",math.ceil(b))

#temp conversion from F to C
blrTempF = 78
k=round(5/9,4); 
blrTempC=(blrTempF-32)*k #math formula for F to C conversion
print("\n")
print("BLR temp in Fahrenheit:", blrTempF, "and in Celcius:", blrTempC)

