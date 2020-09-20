# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:01:34 2020

@author: Asus
"""

#Subject:Lambda 

#Lambda ifadeleri   
x = [1, 2, 3, 4, 5]
result = map(lambda a: a * a, x) #a girdisini alıp a*a işlemi yapıyor fonksiyonu tanımlayıp mape verdim
print(list(result)) 

#map fonk 
a = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]

result = map(len, a)
for i in result:
    print(i, end= ' ')

#birden fazla argümanı lambda nesnesine vermek 
f = lambda a, b: a + b  #burada f callable oldu iki argümanlı fonksiyona benziyor
result = f(10, 20)
print(result) 

#parametresiz lambda işlemi  
f = lambda: 100 
result = f()
print(result) 

#kod içerisindeki herhangi bir değişkeni lambdanın returnüne ekleyebiliyorum 
x = 10
f = lambda a: a * x
print(f(10)) 

#lambda operatorunun map ile kullanımı 
a = [2, 6, 9, 1, 7, 8]
l = list(map(lambda x: x > 5, a))
print(l)

#bir fonksiyonun 3 elemanıda lambda ifadesi olabilir 
fs = [lambda a: a ** 2, lambda a: a ** 3, lambda a: a ** 4]
for f in fs:
    print(f(2))

#lambdada if kullanılmaz if yalnız koşul ifadesi olarak kullanılır 
f = lambda a, b: a if a > b else b #bu kısımda if koşul ifadesi
print(f(4, 6))

#lambda: 
f = lambda a = 1, b = 2: a + b
result = f()
print(result)
result = f(100)
print(result)
result = f(100, 200)
print(result)

#****************************************************************************************# 

#Fiter fonksiyonu =>iterable nesneyi fonksiyona verip true değerleri elde etmemizi sağlar 
a = [7, 9, 2, 1, 10]

def foo(x):
    return x > 5

result = filter(foo, a)
print(list(result))

#yukarıdaki kodun filter ile yazım şekli 
a = [7, 9, 2, 1, 10]
result = [i for i in a if i > 5]
print(result)

#filter example
a = [7, 9, 2, 1, 10]

result = filter(lambda i: i > 5, a)
print(list(result))

#eval fonksiyonu => string şeklindeki ifadelere matematiksel işlem yaptırıyor argüman olarak yalnızca str alıyor
s = '3 * (2 + 1)'
print(s)

result = eval(s)
print(result)

#eval ile import edilen fonksiyonu kullanmak
import math
x = 10
s = '3 * (2 + 1) + math.sqrt(x)'
print(s)
result = eval(s)
print(result) #matematiksel işlem yaptırdım 

#eval ile hızlı bir hesap makinesi 
while True:
    s = input('CSD>')
    if s == 'quit':
        break
    result = eval(s)
    print(result)

#eval ile exception kullanımı 
from math import *

while True:
    s = input('CSD>')
    if s == 'quit':
        break
    try:
        result = eval(s)
        print(result)
    except Exception as e:
        print(e)
#exec=>evalden farklı olarak bir ifadeyi değil bir kod bloğunu çalıştırıyor bir değer vermiyor execte aval gibi sadece "str" alıyor
s = """
x = 10
y = 20
result = x + y
print(result)

for i in range(10):
    print(i)
"""
exec(s)

#**************************************************************************************# 
#Pythonda paketler 
#Package:Çok sayıda modülü tek tek import etmek yerine hepsinin toplandığı yere package denir. 
#içerisinde __init__.py dosyası olan dizinlere paket denir.Bu dosya otomatik olarak çalıştırılır 
#Paket içerisindeli modüllere paketismi.modül adı şeklinde erişebilirz. 

 


