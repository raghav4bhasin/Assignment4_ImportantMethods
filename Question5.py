#DEEP COPY

import copy as c

lst_1 = [1, 2, [3, 4], 5]
lst_2 = c.deepcopy(lst_1)
lst_1[2][0] = "ABC"
print(lst_1)
print(lst_2)


'''
Difference Between DEEP and SHALLOW Copy
SHALLOW COPY of an object copies the ‘main’ object, but doesn’t copy the inner objects. The ‘inner objects’ are shared between the original object and its copy.
Unlike the shallow copy, a DEEP COPY is a fully independent copy of an object.
'''
