# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:29:13 2020

@author: Dogancan Torun
"""


#__init__ metodu anlatım  = javadaki constructor gibi ilk çalıştırılan fonksiyon

class Sample:
    def __init__(self):
        print('__init__')
        

s = Sample()        
k = Sample() #2.nesnemi yarattım yine __init__calıstı 

class Sample:
    def __init__(self):
        self.a = 10
        self.b = 20
        

s = Sample() 
print(s.a, s.b)  

#dunder init example tek degisknler tarihi cektim 
class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 1900
        
    def disp(self):
        print(f'{self.day}/{self.month}/{self.year}') #format ops using
d = Date()
d.disp() 

#dunder init değişken atamalı a ve b x ve y nin degerini alıyor
class Sample:
    def __init__(self, x = 10, y = 20) :
        self.a = x 
        self.b = y
        
        
s = Sample()
print(s.a, s.b)

#dunder_init örnek 
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))
        
        
d = Date(10, 12, 2020)
k = Date(21, 3, 1999)

d.disp()
k.disp() 

#init fonksiyonu 
class Person:
    def __init__(self, name, no):
        self.name = name
        self.no = no
        
    def disp(self):
        print(self.name, self.no)
        
        
per = Person('Dogancan Torun', 1234)
per.disp()

Person.disp(per) #2.tipte fonksiyon cagırma şekli 

#date time modülünün kullanımı 
import datetime
d = datetime.date(2020, 10, 12) 
print(d.day, d.month, d.year)

#date time modulunun ozelligi => gün olarak yazdırdım =>weekday ile günü ogrendim 
import datetime

d = datetime.date(2020, 7, 26) 
print(d.day, d.month, d.year) 
days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
print(days[d.weekday()]) #weekday metodunun kullanımını  pekistirdim  

#Sınıf calışması klavyeden tarih al(dd/mm/yy formaında olsun) modulsuz günü bul 
import datetime

text = input('Lütfen dd/mm/yyy formatında bir tarih giriniz:')
day, month, year = [int(s) for s in text.split('/')]#/ dan ayırdım ve int e cast ettim 

d = datetime.date(year, month, day)
days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']

print(days[d.weekday()]) 

#ctime methodunun kullanımı 
import datetime

text = input('Lütfen dd/mm/yyy formatında bir tarih giriniz:')

day, month, year = map(int, text.split('/'))
d = datetime.date(year, month, day)

print(d.ctime()) #daha detaylı gosterim yaptım  

#date time modülü ile kıyas yapmak  
import datetime

d = datetime.date(2020, 10, 20)
k = datetime.date(2020, 10, 20)

if d > k:
    print('d > k')
elif d < k:
    print('d < k')
elif d == k:
    print('d == k')

#datetime modülü içindeki date time sınıfında saniyeye kadar zaman tutulur 
import datetime
d = datetime.datetime(2020, 7, 26, 19, 12, 25) #datetime sınıfından d nesnesini turettim
print(d)

#sınıfların mutable olduğunu anlatan örnek 
class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
s = Sample(10, 20)
print(s.a, s.b)

s.a = 30
s.b = 40
print(s.a, s.b) 

#sınıfların mutable olduğunu anlatan örnek 2 
class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def disp(self):
        print(self.a, self.b)
        
def foo(s):
    s.a = 100
    s.b = 200
    
s = Sample(10, 20)
s.disp()
foo(s)
s.disp()