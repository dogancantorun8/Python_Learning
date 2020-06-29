# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:04:22 2020

@author: Dogancan Torun
"""


#Subject :For loop definition and using objects 

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
