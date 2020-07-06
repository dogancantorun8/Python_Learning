# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:15:21 2020

@author: Dogancan Torun
"""

#Subject : Conditional Operator  


#Conditional Operator declaration 
val = int(input('Enter a number :'))

result = 100 if val > 0 else 200   #Definition 
print(result)  

#Conditional Operators definition second example
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

max = (a if a > c else c) if a > b else (b if b > c else c)
print(max) 

#Conditional Operators
a = int(input('a:'))
print('even' if a % 2 == 0 else 'odd')  

a =  [12, 3, 4, 5, 9, 8, 21]

#Conditional Operators utilize list
for i in a:
    print('{} ---> {}'.format(i, 'even' if i % 2 == 0 else 'odd'))