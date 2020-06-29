# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:24:30 2020

@author: Dogancan Torun 
"""

#String definition 
s="nairobi-tokyo"   

#String-slicing 
print("Slicing string ={} " .format(s[:7]))    
print("Slicing string ={} " .format(s[13:7:-1])) #output reverse "tokyo" 

#*************************String Methods************************************** 


print("Methods Output:")
#.find values => find member dict  
s2='lacasedepapele' 
print(s2.find('a'))  # the method output index of member  

#count => this method count a character in string 
print(s2.count('a'))

#split method: This is very important methods for string  this get string and return list 
s3='rio,denver,stockholm,moscow'  
print(s3.split(','))  

#find method : this find object or members in string 
print(s2.find("a")) 

#is methods:isalnum,isalpha,islower,isupper   the return values this function bool 
print(s2.isupper())   
print(s2.islower()) 
print(s2.isalnum()) 

#strip  method :trimming string
trims = 'xxxxxyyyyyyyyyxxxxxx atiba hutcinson xyxyxyxyxyyxyxyxxxxx'  
print("Trimming output = {} " .format(trims.strip('xy')))   

#replace method:replace   
print("Trimming output = {} " .format(trims.replace('xy','$')))  

#join method: combine operation 
s400= '#'.join(['jack', 'jones', 'gonzalez', 'stephen', 'zweig'])
print("Joining Output = {} " .format(s400))  

#partition operation : this function  slicing three part 
m='dogancantorunbesiktas' 
z=m.partition(('dogan'))  
z1=m.partition(('torun'))  
z2=m.partition(('besiktas')) 
print(z) 
print(z1) 
print(z2) 

#starts width functions  : this functions return bool 
s = 'spain' 
print(s.startswith('an')) 
print(s.endswith('in'))  



















