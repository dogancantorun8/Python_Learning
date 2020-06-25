# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:44:15 2020

@author: Dogancan Torun 
""" 

#Subject:  Dictionary  
#Key must be hashable but value is not be hashable  
#Key must be unique
#if We have a values we will not get keys

d1={'dogan':25.6,'jonas':'martha','ulrich':[1,2,3],'michael':(5,6,4)} 
print(type(d1)) 


#if you will get value you write keys not write index
print("Ouput of dict= {}" .format(d1['michael']))   
print("Ouput of dict -key2 = {}" .format(d1['jonas']))   

#Another options calling get not throw exception
print("Another calling Ouput of dict -key3 = {}" .format(d1.get('ulrich'))) 

#Changing value 
d1['dogan']=[999,99,9]  
print("Changing dict = {}" .format(d1['dogan'])) 

#if assigning new key and value you will add a dict 
d1['hannah']='katharine'  
print("Adding pair members  dict = {}" .format(d1)) 

#if iterate dict you will get only keys
create_list=list(d1) 
print("Keys list={}" .format(create_list))     

#Multiple values definition 
dm={'atiba':(13,'canada',34),'elneny':(15,'egypt',28),'ruiz':(4,'spain',31),'vida':(24,'croita',30)}  

#Unpacking multiple dicts 
number,nation,age=dm['atiba'] 
print("Information footballers={} {} {}" .format(number,nation,age))

#Creating random dict  two each groups
tup=(('adam',45),(20,40),'xy',range(2)) 
d3=dict(tup)
print("Random dict={}" .format(d3)) 

#Dict functions 

#Len method:Give a pair of key-values 
print("Length dict={}" .format(len(d3))) 

s







 















