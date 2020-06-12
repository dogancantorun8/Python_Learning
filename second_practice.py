# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:36:00 2020

@author: Dogancan Torun
"""


#06 June lecture 
# List function & Range- Iterable Objects & tuples

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

# =============================================================================
# same_list.sort()
# print("Descending Reverse List= {} " .format(same_list)) 
# =============================================================================






