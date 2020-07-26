# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:19:06 2020

@author: Dogancan Torun
"""


#################  OOP Giriş   ############################

#class tanımlama 
class Sample: #interpreter 10 çıktısını çalıştırıyor
    x = 10
    print(x)
#sınıfın değişkenini kullanma
class Sample:
    x = 10
    print(x)

print(Sample.x) #sınıf ismiyle çagırıyorum 

#farklı class değişkenlerini çağırdım
class Sample:
    x = 10
    
class Mample:
    x = 20

print(Sample.x)
print(Mample.x)

#sınıf içerisindeki fonksiyonu çağırma 
def foo():
    print('foo')

class Sample:
    x = 10
    
    def bar():
        print('bar')
    

print(Sample.x)
Sample.bar()

#farklı farklı yerlerdeki  degiskeni cagırma 
x = 20
class Sample:
    x = 10
    
    def bar():
        print('bar')
    

print(Sample.x)
Sample.bar()
print(x)

#Sınıf isimlerinin türü:
class Sample:
    pass

print(type(Sample))
print(type(int))

#sınıf türünden nesne yarattım ve nesnenin türü sample oldu
class Sample:
    pass

s = Sample()
print(type(s))

#tip kontrol nesne ve sınıfın tipi
class Sample:
    pass

s = Sample()

print(type(Sample)) #sınıfın tipi type oldu
print(type(s)) #nesnenin tipi  sınıf ile aynı oldu

#class attribute ve instance attribute farkı 
class Sample:
    x = 10

s = Sample()
s.a = 10  #nesnenin içinde bir örnek öz niteliği yarattım 
s.b = 20
print(s.a, s.b) 
print(type(s.a)) #s sample tipindeyken s.a int tipte bir şeydir
print(Sample.x)


#aynı sınıftan iki nesnenin farkı özniteliklere sahip olması 
class Sample:
   pass

s = Sample()
s.a = 10
s.b = 20.2

k = Sample()
k.x = 100
k.y = 'ali'
print(s.a, s.b)
print(k.x, k.y)

#date sınıfı kullanımı
class Date: 
    pass

date = Date() #class tipinde bir nesne oluşturdum 
date.day = 10 #instance attribute 
date.month = 12
date.year = 2009

print(date.day, date.month, date.year)
print(f'{date.day}/{date.month}/{date.year}')

#complex sayı oluşturma örneği
class Complex:
    pass

z = Complex()
z.real = 10
z.imag = 20

print('{}+{}i'.format(z.real, z.imag))

#example person 

class Person:
    pass

per = Person()
per.name = 'Ali Serçe'
per.no = 123

print(per.name, per.no)

#aynı isimde farklı farklı değişken tanımlama 
x = 10

class Sample:
    x = 20
    
def foo():
    x = 30
    print(x)
    
s = Sample()
s.x = 40

print(x)
print(Sample.x)
foo()
print(s.x)

#classın icine method yazıyorum  VE parametre sayılarına göre çağırılıyorlar
class Sample:
    def foo(self):
        print('Sample.foo')
    
    def bar(self, a, b):
        print('Sample.bar')
    
    def tar():
        print('Sample.tar')
    
        
Sample.foo(0)
Sample.bar(0, 1, 2)
Sample.tar()

#classın icindeki sınıfı cagırma parametrelerini verme 
a = [10, 20, 30]
a.append(100) #tek parametrerli cagırma
print(a)

list.append(a, 100) #ikiside aynı anlama geliyor
print(a)

#clasın icindeki sınıfı cagırma sozluk ornegi 
d = {10: 'ali', 20: 'veli', 30: 'selami'}

val = d.get(20)
print(val)

val = dict.get(d, 20)
print(val)

#string örnegi ve parametre örnegi
s = 'ali'

k = s.upper()
print(k)

k = str.upper(s)
print(k)

#kendi sınıflarımızla methodları cagırma: 
class Sample:
    def foo(self):
        print('Sample.foo')
        
    def bar(self, a):
        print('Sample.bar')
        
s = Sample()

s.foo() #nesneyi  yaratıp foo yu cagırıyorum self nesnesini otomatik ayıkıyor
Sample.foo(s)

s.bar(10)
Sample.bar(s, 10) #same calling 

#s ve self'in aynı nesneyi gosterdigi ornek
class Sample:
    def foo(self):
        self.a = 10
        self.b = 20
                     
s = Sample()
s.foo()
print(s.a)
print(s.b)

#s ve self aynı nesne
class Sample:
    def foo(self):
        self.a = 10
        self.b = 20
                     
s = Sample()
s.foo()
print(s.a) # s ve self esdeger nesneler oldugu icin s.a da aynı şeyi gsterdi
print(s.b)

k = Sample()
k.foo()
print(k.a)
print(k.b)

#a ve b argümanlarına değer dinamik tür sistemine göre değer atama
class Sample:
    def set(self, a, b):
        self.a = a
        self.b = b
                     

s = Sample()
s.set(10, 20)        # Sample.set(s, 10, 20) burda s selfe gidiyor 10 a ya 20 b ye gidiyor
print(s.a, s.b)

#a ve b argümanlarına değer dinamik tür sistemine göre değer atama ve ekrana basma
class Sample:
    def set(self, a, b):
        self.a = a
        self.b = b
        
    def disp(self):
        print(self.a, self.b)
                     

s = Sample()

s.set(10, 20)        # Sample.set(s, 10, 20)
s.disp()             # Sample.disp(s)

#iki farklı nesne üretip onları ekrana basma 
class Sample:
    def set(self, a, b):
        self.a = a
        self.b = b
        
    def disp(self):
        print(self.a, self.b)
                     

s = Sample()
k = Sample()

s.set(10, 20)
k.set(30, 40)
s.disp()
k.disp()



