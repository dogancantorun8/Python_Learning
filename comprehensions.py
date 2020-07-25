# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:57:10 2020

@author: Dogancan Torun
"""

#Comprehensions: 
#1)List comprehensions 
#2)Set comprehensions
#3)Dict comprehensions 


##############List comprehensions: 
a = [i * i for i in range(10)] #==> Result return list 
print(a) 

# equal below list comprehensions
a = []
for i in range(10):
    exp = i * i
    a.append(exp)
    
print(a) 

#############list comprehensions second example 
a = [10 for i in range(10)]
print(a)

#equal below list comprehensions
a = []
for i in range(10):
    exp = 10
    a.append(exp)
    
print(a)

################list comprehensions example 3
s = '10,20,30,40,50'

a = [int(num) for num in s.split(',')]
print(a)

#equal below list comprehensions
a = list(map(int, s.split(',')))
print(a) 

#list comprehensions example 4  
s = '10,20,30,40,50'
a = list(map(int, s.split(',')))
print(a)

vals = [3, 4, 6, 5, 8, 10, 12]
result = [i % 2 == 0 for i in vals]
print(result)

#list comprehensions example 5
names = ['john', 'mike', 'lee', 'hans', 'perreira']
a = [name[::-1] for name in names]
print(a)

###########################list comprehensions with if : 
x = [2, 5, 8, 6, 4, 9, 12]

a = [i for i in x if i % 2 == 0]
print(a)

#equal below list comprehensions
x = [2, 5, 8, 6, 4, 9, 12]
a = []
for i in x:
    if i % 2 == 0:
        a.append(i)
        
print(a) 

#second solution   below list comprehensions
x = [2, 5, 8, 6, 4, 9, 12]

print(*[i for i in x if i % 2 == 0], sep=', ')

#print starts a example list coprehensions
names = ['john', 'mike', 'lee', 'hans', 'perreira','Adams']
a = [name for name in names if name[0].lower() == 'a']
print(a)

#upper example 
cities = ['manchester', 'bitlis', 'barceleno', 'rome', 'paris']

a = [city.upper() for city in cities]
print(a)

#find "a" and upper operations 
cities = ['manchester', 'bitlis', 'barceleno', 'rome', 'paris']

a = [city[:3].upper() for city in cities if 'a' in city]
print(a)


#list comprehensions palindrom
texts = ['anastas mum satsana', 'salih', 'kabak', 'ali', 'ey edip adanada pide ye','ali']

palindromes = [s for s in texts if s == s[::-1]]
print(palindromes)

#string palindrome check numbers

numbers = [12, 1221, 13431, 12345, 197262]
result = [number for number in numbers if str(number) == str(number)[::-1]]
print(result)

#tuple slicing with list comprehensions
cities = [('barcelona', 6), ('kiev', 35), ('moscow', 26), ('prague', 48), ('pekin', 37)]
result = ['{}-{}'.format(plate, name) for name, plate in cities]
print(result)

#prime numbers list comprehensions with using functions
def isprime(val):
    if val % 2 == 0:
        return val == 2
    for i in range(3, val, 2):
        if val % i == 0:
            return False
    return True

result = [i for i in range(2, 1000) if isprime(i)]
print(result)

#dublicate index check 

a = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]

result = [a[i] for i in range(0, len(a), 2)]
print(result)

#nested for list comprehensions 
a = [[1, 20, 3], [21, 87, 8, 10], [5, 9, 6, 44]]

result = [y for x in a for y in x if y >= 20] #nested for "for x in a" =outside for
print(result)

#çift sayılar için nested  içlem  
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [[y for y in x if y % 2 == 0] for x in a]
print(result)

###############################Set comprehensions ############################# 
#set comprehensions
s = {ch for ch in 'madrid'}
print(s)

#eşdeğeri
s = set('madrid')
print(s)

#bütün olası ikili toplamları buluyor
a = [2, 1, 12, 2, 3]

b = {x + y for x in a for y in a}
print(b)

##################dict comprehensions ####################### 
#dict comprehensions
d = {i: str(i) for i in [1, 2, 3, 4, 5]}
print(d)

#change key-values  
cities = [('barcelona', 6), ('kiev', 35), ('moscow', 26), ('prague', 48), ('pekin', 37)]
d = {value: key for key, value in cities}
print(d)

#dict example 
l = [('josh', 123, 1982), ('mikel', 65, 1970), ('marienne', 340, 1990), ('ayşe', 71, 1969)]
d = {name: (no, year) for name, no, year in l}
print(d)