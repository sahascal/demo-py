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

