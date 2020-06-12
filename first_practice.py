# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:56:56 2020

@author: Dogancan Torun
"""

#30-31 May lecture replication 
#Subject=Introduction to data structure & List definition & Type casting 

letter=input("Enter  letter =")  
number=input('Enter  number =')

my_list=['Ali',[10,'a',15,[8,20]],0,45,'mehmet']   

#Assignee new list 
my_list2=my_list[1][1]
print(my_list2) 
my_list3=my_list[1][3][1]
print(my_list3)    
my_list4=my_list[1][3]
print(my_list4)  
print(type(my_list4))


#Mathematical operations and type casting 
print("**Mathematical blog output***")
print (int(number)+5) 

#string operations
print(letter+"can")   

#Negative index operation 
print(int(number) + my_list[-2]) 

#List reverse not use "reverse" function
reverse_list=my_list[ : : -1] 
print(reverse_list) 


#is control block
print(my_list3 is letter) 








