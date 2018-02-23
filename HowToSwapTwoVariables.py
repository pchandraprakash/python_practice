""" How to swap two variables? """
v1 = 'variable 1'
v2 = 'variable 2'

# (wrong)Solution 1
"""Many tend to use this trick but this won't work because when we say v1 = v2, the pointer v1 will be directed towards
value that v2 refers and when we say v2 = v1, both v1 and v2 are pointing at same values"""
v1 = v2
v2 = v1
print(v1)
print(v2)

# correct solution 2
a = 1
b = 2

# create two temporary variables t1,t2 pointing to a,b. which means values of a,b
t1 = a
t2 = b

# now swap the values of t1 and t2 across a and b
a = t2
b = t1

print(a)
print(b)

# correct solution 3
var_1 = "First Variable"
var_2 = "Second Variable"

temp = var_1
var_1 = var_2
var_2 = temp

print(var_1)
print(var_2)
