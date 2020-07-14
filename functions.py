# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:11:59 2020

@author: Dogancan Torun 
"""

#Functions  Declaration


#No arguments functions declaration and calling
def foo():
    print('foo')

foo()  #calling 
print('ends...')  




#Assigning foo another function
def foo():
    print('foo')
    
print(type(foo))

foo()
bar = foo
bar() 


#Nested functions 
def foo():
    print('foo')
    
def bar():
    print('bar')
    foo()
    
bar() #if we calling bar we will print foo
print('ends..')


#Fuction declaration arguments and calling 
def foo(a, b):
    print('{} -> {}'.format(a, type(a)))
    print('{} -> {}'.format(b, type(b)))
    print('-------------------------')
  
foo(10, 20)
foo(10, 'atiba')
foo('jack', 12.4)  

#functionn 
def banner(s):
    print('-' * len(s))
    print(s)
    print('-' * len(s))
       
banner('barcelona')  

#Shape functions 
def disp_shape(height, width):
    pos = 0
    direction = 1
    for i in range(height):
        print('|' + ' ' * pos + '*' + ' ' * (width - pos -1) + '|')
        if pos == width - 1:
            direction = -1
        elif pos == 0:
            direction = 1
        pos += direction       
disp_shape(20, 4)  

#return operator
def square(a):
    print('square running...')
    #return a * a


x = square(10)
print(x) 

#the function has not return so not assignment x 
def foo():
    print('foo')
    
x = foo()
print(x)  

#many argumant return  tuple
def foo(a):
    print('foo')
    return a ** 2, a ** 0.5  #many values return 
    
a, b = foo(10)
print(a, b) 

#Return different types 
def foo(a):
    if a > 0:
        return a * a
    else:
        return 'negative value'
    
result = foo(10)
print(result)

result = foo(-10)
print(result) 



#Second order equation 
def solve(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    
    return x1, x2

result = solve(1, 0, -4)
if result == None:
    print('Not root')
else:
    x1, x2 = result
    print('x1 = {}, x2 = {}'.format(x1, x2)) 



#buble sort alghoritms 
def bsort(a):
    for i in range(len(a) - 1):
        for k in range(len(a) - 1 - i):
            if a[k + 1] < a[k]:
                a[k + 1], a[k] = a[k], a[k + 1]

a = [4, 8, 1, 9, 6]
bsort(a)
print(a)

#iterable function defining 
def getsum(iterable):
    total = 0
    for i in iterable:
        total += i
        
    return total

t = getsum([10, 20, 30, 40])
print(t)

#iterable tuple returning 
def get_sum_avg(iterable):
    total = 0
    for i in iterable:
        total += i
        
    avg = total / len(iterable)
        
    return total, avg

t, avg = get_sum_avg([10, 20, 30, 40])
print(t, avg)

#list returning 
def get_odd_even(iterable):
    odd = []
    even = []
    for i in iterable:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    return odd, even

odd, even = get_odd_even([1, 2, 3, 4, 5, 6, 7])
print(odd)
print(even)  

#standart deviation example
def get_mean_stddev(iterable):
    total = 0
    for i in iterable:
        total += i
    mean = total / len(iterable)
    
    total = 0
    for i in iterable:
        total += (i - mean) ** 2
        
    stddev = (total / len(iterable)) ** 0.5
    
    return mean, stddev

mean, stddev = get_mean_stddev([1, 2, 3, 4, 5])
print(mean)
print(stddev) 


