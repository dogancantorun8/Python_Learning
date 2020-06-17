# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:36:01 2020

@author: Dogancan Torun 
"""
#List Unpacking & Tuples & Tuples Unpacking 
main_list=[10,20,'Dogan',['ozgur','abdullah',32,65],'cemre',40,22]  

#Partition_List
partial_list=main_list[2:5]
print("Partial List={} " .format(partial_list))  

#List Unpacking  
unpack_list=[a,b,c]=partial_list 
print("Unpacking first index= {} " .format(unpack_list[0]))  

#Create Matrix using List => 3x3 square matrix 
three_square_matrıx=[[1,2,3],[7,8,9],[0,6,11]] 
print("Matrix={} " .format(three_square_matrıx)) 

######### Introduction to Tuples ######################## 
print("### Introduction to Tuples ###")
my_tuple=('jack',[95,27,'marienne'],'tony',99,20)  

#Another Tuple Definition  
t = 'Ali', 123, 'Veli', 34.6 
print(type(t))  
print(20 in t)   

#Unpacking Tuples
(x,y,z,m)=t 
print("First index= {} ".format(x)) 
print(type(x))   
print("Fourth index= {} ".format(m))  
print(type(m))   



#Tuple mathematical operations 
add_tuple=my_tuple+t 
print("Adding output={}" .format(add_tuple)) 

#Tuple Swap Operations 
add_tuple,t=t,add_tuple 
print("After the swap operations={}"  .format(add_tuple)) 








 

 



# =============================================================================
# partial_tuple(x,y)=my_tuple(0:1) 
# print("Partial Tuple={} " .format(partial_tuple))  
# =============================================================================








 





