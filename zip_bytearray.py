# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:08:53 2020

@author: Dogancan Torun
"""


#Subject:Zip and byte&byte arrays 

################zip functions################################################ 
#zip decleration :built-in python function 
a = [1, 2, 3, 4, 5]
b = ('mikel', 'essien', 'josh', 'ryan', 'ronaldo')

c = zip(a, b) #give iterable object 

x = list(c) #list yoluyla iterate ediyorum 
print(x)

#zip 

for x, y in zip('ankara', 'edirne'):
    print(x, y)

#3 lu zip 
a = [10, 20, 30]
b = ['jonas', 'mikel', 'josh']
c = [1.2, 5.6, 7.8]

d = zip(a, b, c)
for t in d:
    print(t)
    
#zip fuction care  shortlist
a = [10, 20, 30, 40, 50]
b = ['ali', 'veli', 'selami']
c = [1.2, 5.6]
 
d = list(zip(a, b, c))
print(d)
    
    
#zip example :achieve 3 member  tuples
for x, y, z in zip(range(0, 5), range(10, 15), range(20, 25)):
    print(x, y, z)

#same unzip operations 
a = [('vida', 10), ('elneny', 20), ('atiba', 30), ('ljaic', 40), ('roco', 50)]

x, y = zip(*a)#that means iterate a objects =opposite of zip

print(x)
print(y) 


#achieve list a list:
a = [('vida', 10), ('elneny', 20), ('atiba', 30), ('ljaic', 40), ('roco', 50)]

l = [list(t) for t in zip(*a)]
print(l) 

##python permutation and combination operation#################### 

#python standart kutuphanesı ıcersıınde itertools modulu icerisinde permutations ve combinations isimli fonksıyonlar bır kumenın permutasyon ve kombınasyonunu verır bize. Bu fonksiyonlar bize ıterabloe bir nesne verir dolayısıyla bızım bunları iterate etmemız gerekmektedır.Parametre olarak iterable bir nesne alır ve kaclı komb veya permutasyonunu ıstersın diye 2 tane parametresı var. Iterable ederken de her iterasyoda bir demet elde ederız bu demetler de onun per veya komblarını gosterır.
#combination example
import itertools

a = ('mikel', 'gordon', 'simpson')

b = itertools.combinations(a, 2) #that means C(3,2)

for t in b:
    print(t) 

#permutation
import itertools

a = ('marienne', 'jane', 'martha')

b = list(itertools.permutations(a, 3))
print(b) 

#bytes declaration and iteration : 
b = b'\x01\x02\x03\x04\x05'

for i in b:
    print(i)

#-------------------------------------------

b = b'barcelona'
a = list(b)
print(a)

#bytes ankarayı elde ettim 
a = ''.join([chr(i) for i in b])

print(a)


#show ascıı code
b = bytes([10, 20, 30, 40, 50])
print(b)

#bytes array definition 

ba = bytearray(b'barceleno')
print(ba)

#show ascıı code
ba = bytearray([1, 2, 3, 4, 5])
print(ba)

#bytes convert to string with encoding type 
b = b'barcelona'
s = str(b, encoding='UTF8')
print(s)

#encode characters using byte
s = 'madrid'
k = s.encode()
print(k)
