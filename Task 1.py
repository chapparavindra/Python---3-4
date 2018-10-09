# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:08:52 2018

@author: cravindra
"""

#1.1
'''Write a Python Program to implement your own myreduce() function which works exactly like
Python's built-in function reduce()'''
def Multiply(x,y): return x * y
def myreduce(anyfunc, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = anyfunc(result, item)
    return result



print(str(myreduce(Multiply, [5,5,5,5])))

#1.2
'''Write a Python program to implement your own myfilter() function which works exactly like
Python's built-in function filter()'''
def myfilter(anyfunc, sequence):
    result = []
    for item in sequence:
        if anyfunc(item):
            result.append(item)
    return result

def iseven(x):
    if (x%2== 0): 
        return True 
    else: 
        return False


print(str(myfilter(iseven, [28,1,2,11,22,16])))

#1.3Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
word = "ACADGILD"
#Iterating Each Character in the String
alphabet_list = [ alphabet for alphabet in word ]
print (str(alphabet_list))



#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
x = ['x','y','z']
#Creating a List using Comprehension list technique and nested for Loop
result = [ item*num for item in x for num in range(1,5)  ]
print(str(result))


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
y = ['x','y','z']
#Creating a List using Comprehension list technique and nested for Loop
result = [ item*num for num in range(1,5) for item in y   ]
print(str(result))



#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
z = [2,3,4]
result = [ [item+num] for item in z for num in range(0,3)]
print(str(result))

[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
listset = [2,3,4,5]
result = [ [item+num for item in listset] for num in range(0,4)  ]
print(str(result))

[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
listset=[1,2,3]
result = [ (b,a) for a in listset for b in listset]
print(str(result))

#1.3 Implement a function longestWord() that takes a list of words and returns the longest one.
from functools import reduce
#Function that will return the Largest word from the list
def longestWord(lst):
    largestvalue=''
    #if list has more than one item thenit will compare using reduce method using two item a item else it will return the first Item
    if (len(lst)>1):
        largestvalue=reduce(lambda x,y: x if len(x)>len(y) else y,lst)
    else:
        largestvalue=lst[0]
    return largestvalue


print(longestWord(['Raja','Ravi','Bhavya','Varnikasai','chapparavindra']))


