# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:57:09 2020

@author: Dogancan Torun
"""

#Subject:Set Operations-Methods and Frozenset  

#Set definition
s={10,20,30,'ali',(1,2,3)}  
s2=set([20,60,30,'mehmet',(9,0,8)]) #another definition set

#print(s[0]) not get any member of set 
print(20 in s) #member control block  

cast_list=list(s) 
print("Casting list={}" .format(s))   

#Set Operations 
print("Subset control= {} " .format(s.issubset(s2)))   
print("Superset control= {} " .format(s.issuperset(s2)))  
print("Intersection operation = {} " .format(s.intersection(s2)))  
print("Union operation = {} " .format(s.union(s2)))   
print("Difference control = {} " .format(s.difference(s2)))   

#Set Methods 
s.add(99)
print("Add a member set {} " .format(s) )   
s.update(range(100,105,2))  
print("Iterable add  operations {} " .format(s) )  
s.remove((1,2,3))  
print("After  the removing={} " .format(s))    
s.clear()  
print("All members delete operation={} " .format(s))   

#Frozenset definition 
fs=frozenset([5,55,555,5555,'ali',20,60,(9,0,8)]) 
#fs={a,b,c} 
print(type(fs)) 
print(fs)  

#frozenset operations  
print("FS Subset control = {} " .format(fs.issubset(s2))) 
print("FS Superset control= {} " .format(fs.issuperset(s2)))  
print("FS Intersection operation = {} " .format(fs.intersection(s2)))    
print("FS Union operation = {} " .format(s.union(s2))) 
print("FS Difference control = {} " .format(fs.difference(s2)))   


 













  














  




    









 



