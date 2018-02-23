a = ['Apple', 'Banana', 'Microsoft']
# solution 1
temp = a[0]
a[0] = a[2]
a[2] = temp
# solution 2
a[0], a[2] = a[2], a[0]

print(a)

num_list = list(range(1, 6))
for i in range(len(num_list)):
    for j in range(i + 1):
        print(num_list[i])




