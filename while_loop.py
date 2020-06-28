# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:41:10 2020

@author: Dogancan Torun
"""

#While Loop =>Definition while loop and example

#while condition => indent level  
print("ındent level outputs")
i = 0
while i < 10:
    print(i)
    i += 1 
    print("*")
print('end') 


#while  n*(n+1)/2 definition 
n = int(input('Enter a  number formulas:'))
j = 1
total = 0
while j <= n:
    total += j
    j += 1   
print(total)  


#while negative iteration  
i = 10
while i:
    print(i)
    i -= 1  #i--

#while sweeping iteration 
a = [10, 20, 30, 40, 50, 60]
i = 0
while i < len(a):
    print(a[i])
    i += 1
      


#Create a list via while loop and you will enter a "0" ,while loop end
a = []
val = True
while val:
    val = int(input('Enter a number :'))
    a.append(val)
print(a)  

#String character printing block 
s = 'barcelona'
i = 0
while i < len(s) :
    print("String character printing={}" .format(s[i]))
    i += 1

#Square operation 
a = [1, 2, 3, 4, 5]
i = 0
while i < len(a):
    a[i] = a[i] ** 2 #square operation
    i += 1    
print(a) 

#Count even numbers in array 
a = [3, 5, 7, 9, 5, 7, 12, 87, 92, 44]
i = 0
even = 0
while i < len(a):
    if a[i] % 2 == 0:
        even += 1
    i += 1    
print(even) 

#Manuel ıtem with while loop 
a = [('denver', 100), ('moscow', 200), ('josh', 300)]
d = {}
i = 0
while i < len(a):
    key, val = a[i] #assigning couple key value 
    d[key] = val
    i += 1    
print(d) 


#Key  check operation  
a = [('jason', 100), ('alex', 200), ('lee', 300), ('jane', 400)]
d = dict(a)    
name = input('Enter a name :')
if d.get(name):
    print(f'Değeri: {d[name]}')
else:
    print('Key not found ') 


#while manuel packing 
s = 'madrid'
while s:  # string iterate 
    print(s)
    s = s[1:] 

#while string enterpolasyon 
a = list(range(10))
i = 0
while i < len(a):
    print(i, end=' ')  #Format  printing 
    i += 1 

#Max function in array 
a = [10, 4, 56, 23, 4, 9, 90, 23, 76]
max = a[0]
i = 1
while i < len(a):
    if a[i] > max:
        max = a[i]
    i += 1      
print(max) 

#Manuel list reverse
a = [10, 4, 56, 23, 4, 9, 90, 23, 76]
i = 0
while i < len(a) // 2:
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    i += 1   
print(a) 
