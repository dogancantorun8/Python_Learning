# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:04:22 2020

@author: Dogancan Torun
"""


#Subject :For loop definition and using objects an break continue 

my_list = [10, 20, 30, 40, 50]

#for using list 
for i in my_list: #for need iterable object 
    print(i , end=' ')   


#for using range function
r = range(10)

for i in r:
    print(i,end=' * ') 

#Get dict's  keys 
d = {100: 'lebron', 200: 'osman',300:'james',400:'marienne'}
count=1
print("\n")
for i in d:
    print("Printing keys {} ={} " .format(count,i))   
    count +=1 

#Get dict's keys and values 
count2=1;
for key, value in d.items():
    #print(key, value)
    print("Keys and values {} ={} " .format(count2,key, value)) 
    count2 +=1 

#Iterate tuple  and output 
a = [('ljaic', 10), ('necip', 20), ('marcelo', 30), ('dogan', 40), ('ozgur', 50)]
for t in a:
    print(t)  

#Iterate tuple and unpacking 
a = [('ljaic', 10), ('necip', 20), ('marcelo', 30), ('dogan', 40), ('ozgur', 50)]


for t in a:
    print(t)
a = [('ljaic', 10), ('necip', 20), ('marcelo', 30), ('dogan', 40), ('ozgur', 50)]

#tuple unpacking operations
for name, no in a:
    print(name, '--', no) 
    

#for list operations
m = [10, 20, 30, 40, 50]


for i in range(len(m)):
    m[i] = m[i] * 2

print(m) 

#for using set  
s = {'jamon', 'lucas', 'gordon','dimitris','diamantidis','arroyo'}

for i in s:
    print(i) #printing but not same s  

#give a direct list    
for i in (1, 3, 5, 7, 9):
        print(i**3,end=' ')   

#Create tuple ,tuple has two members
for i in range(10):
    for k in range(10):
        print('({}, {})'.format(i, k), end = ' ')  

#key-value swapping operations
d = {'dogan': 120, 'atiba': 200, 'elneny': 300, 'vida': 40, 'diaby': 50}        
k = {}

for key, value in d.items():
    k[value] = key
    
print(k)  

#Odd even list operations
a = [3, 6, 7, 8, 34, 56, 57, 99, 34]
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(even)
print(odd) 

#Standart Deviation  
a = [3, 6, 7, 8, 34, 56, 57, 99, 34]
mean = sum(a) / len(a)

total = 0
for x in a:
    total += (mean - x) ** 2
    
stdev = (total / len(a)) ** 0.5
print(stdev)  

#String iteration example 
n = int(input("Bir sayi girin="))
for s in str(n):                  
     print(s, end=' ') 

#break example =>if list has "0" loop break and end loop
a = [10, 4, 5, 0, 7, 9, 8]

for x in a:
    if x == 0:
        break
    print(x)
    
print('ends...')   

#find list members and breaking loops 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]    

val = int(input('Can you find value in list=:'))
for x in a:
    if val == x:
        print('found')
        break
else:
    print('not found!')   

#continue expression only write odd number    
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('ends...') 

#Create cmd console using break and continue with while loop 
while True: 
    print('CSD>', end='')
    cmd = input().strip()
    if cmd == '':
        continue
    if cmd == 'quit':
        break
    if cmd == 'dir':
        print('dir command')
    elif cmd == 'copy':
        print('copy command')
    elif cmd == 'remove':
        print('remove command')
    else:
        print('bad command!')


        


