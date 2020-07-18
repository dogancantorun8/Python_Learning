# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:22:54 2020

@author: Dogancan Torun
"""

#Subject:import and random  operations 


#only import sqrt and log functions
from math import sqrt, log10

x = sqrt(10)
print(x)

x = log10(100)
print(x)


sqrt = 100  #sqrt direct calling
print(sqrt)

import math
x = math.sqrt(10) #sqrt calling by math library 
print(x)

#as => idiom utilizing 
from math import sqrt as s

result = s(10)
print(result)  

#random number creating 0-9 seperation using "randint" methods
import random

for i in range(10):
    x = random.randint(0, 9) #rand intv
    print(x, end=' ')
print() 

#heads tail possibility  example  
import random

def coin(n):
    head = tail = 0
    for i in range(n):
        x = random.randint(0, 1) 
        if x == 0:
            tail += 1
        else:
            head += 1
            
    return head / n, tail / n


head, tail = coin(1000000)
print(f'head: {head}, tail: {tail}')  #string enterpolation 

#random2: 
import random

#create 10 numbers between 0-99 these operations same= rand range 
def getrand(a, b, count):
    result = []
    for i in range(count):
        x = random.randint(a, b) #create 0-99 numbers
        result.append(x)
        
    return result  #return list

x = getrand(0, 99, 10)
print(x)  

#randrange methods using 
import random

x = random.randrange(10, 20, 2)
print(x) 


#randomchoice function => expect iterable object but this function not get sets be careful!! 

import random

names = ['john', 12.3, 'jason', 123, 'hulk']
name = random.choice(names)
print(name) 

#randomshuffle  => shuffle iterable objects members 
import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(a)
print(a) 

#52 cards example  
def create_deck():
    suits = ['Karo', 'Kupa', 'Maça', 'Sinek']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz', 'As']
    deck = []
    
    for number in numbers:
        for suit in suits:
            deck.append(suit + '-' + number)
            
    return deck

deck = create_deck()
print(deck)  

#52 cards example distribute code   
print("Distribition:::")
import random 
def distribute_deck(deck) :
    a=[] 
    b=[] 
    c=[] 
    d=[] 
    random.shuffle(deck) 
    for i in range(0,52,4) :
        a.append(deck[i]) 
        b.append(deck[i+1]) 
        c.append(deck[i+2]) 
        d.append(deck[i+3]) 
        
    return a,b,c,d 
    
a,b,c,d=distribute_deck(deck)
print(a) 
print(b) 
print(c) 
print(d) 

#random.random => calculate pi number use iteration 
import math 
import random 
def get_pi(n) :
    k=0 
    for i in range(n) :
        x=random.random() 
        y=random.random() 
        if math.sqrt(x**2 + y**2 )<1 :
            k +=1 
    return 4*k/n  #this formula calculate unit circle  

pi=get_pi(100) 
print(pi) 

#enumerate function using and declaration: this function return index of iterable objects
#type of x is tuple be careful !
a=['vida','atiba','elneny','diaby'] 
for x in enumerate(a) :
    print(x) 
    
#slicing operations two values but not return tuple 
for index,val in enumerate(a)  :
    print(index,val) 

#How to find greatest number's index  of list  

#classic method
a=[12,6,43,4,9,42,17,30] 
index=0 
max=a[0] 
for i in range(1,len(a)): 
    if a[i]>max :
        max=a[i] 
        index=i 
print(index)        

#find greatest number's index  of list second solution (enumerate): 
a=[12,6,43,4,9,42,17,30] 
max_index=0 
max=a[0]  

for index,val in enumerate(a): 
    if val>max :
        max=val
        max_index=index
print(max_index)   




#use plot library and sketch graphs 
x=[] 
y=[] 
f=-10 
while f<10 :
    x.append(f) 
    y.append(f*f) 
    f +=0.1 

import matplotlib.pyplot as plt 
plt.plot(x,y) 

x=[1,2,3]
y=[4,3,17] 
plt.plot(x,y)  
plt.show()


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()


#Scope: 
x=10 
def foo() : 
    y=100
    print(x)  
    print(y)

foo() 

def bar() : 
    y=150
    print(y) 

bar()

#global function value change
m=1000
def banner() :
    global m 
    m=30 
    print(m) 

banner()    

#Map function => its not important function 
def foo(a) :
    return a*a 

x=[1,2,3,4,5] 
result=map(foo,x) 

for k in result: 
    print(k) 

#map second example 
import math 
x=[1,2,3,4,5]
result=map(math.sqrt,x) 
l=list(result) 
print(l)

#map example 3 
s='100,200,300,400,500' 
#s.split(',') 
x=list(map(int,s.split(',')))
print(x)





