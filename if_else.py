# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:41:12 2020

@author: Dogancan Torun
"""

#Subject:if-else Conditions


#Even odd controls
number = int(input('Enter a number :'))

if number % 2 == 0: 
    print('even')
else: 
    print('odd')   
    
#quadratic root defining      
num1 = float(input('num1:'))
num2 = float(input('num2:'))
num3  = float(input('num2:'))

delta = num2 ** 2 - 4 * num1 * num3
if delta >= 0:
    x1 = (-num2 + delta ** 0.5) / (2 * num1)
    x2 = (-num2 - delta ** 0.5) / (2 * num1)
    print(f'x1 = {x1}, x2 = {x2}')  # print('x1 = {}, x2 = {}'.format(x1, x2))
else:
    print('Not find real root')  
    
    
    
#Basic sort alghorithms
a = int(input('a:'))
b = int(input('b:'))
c = int(input('a:'))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c) 


#Check number block
number2 = int(input('Enter a number:'))
if number2 == 1:
    print('one')
elif number2== 2:
    print('two')
elif number2== 3:
    print('three')
elif number2 == 4:
    print('four')
elif number2 == 5:
    print('five')
else:
    print('other number')  
 


   



    
