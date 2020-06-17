# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:36:00 2020

@author: Dogancan Torun
"""


#06 June lecture 
# List function & Range- Iterable Objects 

main_list=[20,[30,45],'Ali',[40,50,'Dogan'],0,25] 

print("****Outputs****") 
print("Main List = {}" .format(main_list))

#List Function Using 
same_list=main_list.copy() 
print("Copy List= {} " .format(same_list))  

same_list.append(100)  
print("Appending List= {} " .format(same_list)) 

same_list.extend([99,999])
print("Extending List= {} " .format(same_list))  

same_list.reverse() 
print("Reverse List= {} " .format(same_list))  

same_list.remove('Ali')  
print("Remove one member  List= {} " .format(same_list)) 

indeks=same_list.index(100) 
indeks2=same_list.index(99,1)   #Start "1" index and search step 1  


print("İndex find = {}" .format(indeks))   
print("İndex find = {}" .format(indeks2))  


#Range function:If you generate iterable objects you will use this function 
r=list(range(0,18,3)) 
print("Range list={}" .format(r))  

r_reverse_range=list(range(40,20,-4))
print("Reverse_range_list ={}" .format(r_reverse_range)) 







# =============================================================================
# c=main_list[1]   
# print("C List ={} " .format(c.sort(reverse=False)) )
# ============================================================================= 










