""" Compute the sum of all the multiples of of 3 and 5 that are less than 100 """


class Multiples(object):
    def __init__(self, num_list):
        self.num_list = num_list

    def sum_of_mul_3_5(self):
        new_list = []
        for i in self.num_list:
            if i % 3 == 0 and i % 5 == 0:
                new_list.append(i)
                total = 0
                sum_list = []
                for elements in new_list:
                    total += elements
                sum_list.append(total)
        print(new_list)
        print(sum_list)


m = Multiples(list(range(1, 100)))
m.sum_of_mul_3_5()

# Alternative Solution


class Test(object):
    t = 0
    for j in range(1, 100):
        if j % 3 == 0 and j % 5 == 0:
            t += j
    print(t)


t = Test()

"""
sample_list = [5, 4, 3, 3, 2, 1, -1, -3, -5, -7, -8, -10]
print the sum of only negative numbers in this list
"""
sample_list = [5, 4, 3, 3, 2, 1, -1, -3, -5, -7, -8, -10]
list_1 = []
list_2 = []
for elements in sample_list:
    if elements < 0:
        list_1.append(elements)
        total_1 = 0
        for ele in list_1:
            total_1 += ele
list_2.append(total_1)
print(list_1)
print(list_2)
