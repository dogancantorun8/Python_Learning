# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:01:03 2020

@author: Dogancan Torun
"""

#Subject:Pythonda sınıf türetme işlemleri 

#class türetme syntaxı B sınıfı  A dan türedi
class A:
    def foo(self):
        print('A.foo')
        
    def bar(self):
        print('A.bar')

class B(A): #B sınıfını A dan türettim 
    def tar(self):
        print('B.tar') 
        

class C(B): #C sınıfını da B den türettim 
    def car(self):
        print('C.car')
        
              
b = B()
b.foo()
b.bar()
b.tar()

c = C()
c.foo()
c.bar()
c.tar()
c.car()

#Eger C => A dan türetilseydi 
class A:
    def foo(self):
        print('A.foo')
        
    def bar(self):
        print('A.bar')

class B(A):
    def tar(self):
        print('B.tar')
         
class C(A): #C A'dan türetilmiş
    def car(self):
        print('C.car')
        
c = C()
c.foo()
c.bar()
c.car()

#İnheritance ile örnek özniteliği oluşturup çağırma 

class A:
    def foo(self):
        print('A.foo')
        
    def bar(self):
        print('A.bar')

class B(A):
    def __init__(self):
        self.x = 10
        self.y = 20
        
    def tar(self):
        print('B.tar')
         
b = B()
print(b.x, b.y)

#dunder init öznitelik oluşturup kullanma  tek sınıf için
class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
                
a = A()
a.dispA()


#exception oluşacak:b için __init çağrılıyor fakat y yaratılıyor x yaratılmadıgından hata alır
class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
        
class B(A):
    def __init__(self):
        self.y = 20
        
    def dispB(self):
        print(self.y)


b = B()
b.dispA()   #y yaratılıyor fakat dispA x i arıyor hata burdan  kaynaklı

#Yukarıdaki exception olmasın diye B nin içinde A nın __initi çağrılddımı ve hata alma
class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
        
class B(A):
    def __init__(self):
        A.__init__(self) #taban sınıfın __ initini çağırdım
        self.y = 20
        
    def dispB(self):
        print(self.y)

b = B()
b.dispA()               
b.dispB()

# için içiçe __ init kullanımı
class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
        
class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 20
        
    def dispB(self):
        print(self.y)

class C(B):
    def __init__(self):
        B.__init__(self) #taban sınıfın __ initini çağırdım
        self.z = 30
        
    def dispC(self):
        print(self.z)
c = C()
c.dispA()
c.dispB()
c.dispC()

#__init methodlarının çoklu parametre kullanımı 
class A:
    def __init__(self, x):
        self.x = x
        
    def dispA(self):
        print(self.x)
        
class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y
        
    def dispB(self):
        print(self.y)


b = B(10, 20)
b.dispA()
b.dispB()

#Super methodu ile türetilmiş sınıftan base sınıfın __init methodunu çağırma 
class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
        
class B(A):
    def __init__(self):
        super(B, self).__init__()  #super iki parametre alır  # A.__init__(self)
        self.y = 20
        
    def dispB(self):
        print(self.y)

b = B()
b.dispA()
b.dispB()

#Base sınıfın öz nitelikleri türetilmiş sınıfta kullanılan örnek 
class Employee:
    def __init__(self, name):
        self.name = name
        
class Worker(Employee):
    def __init__(self, name, shift):
        Employee.__init__(self, name) #base sınıfın __initi çağrıldı
        self.shift = shift
        
    def disp(self):
        print(f'{self.name}, {self.shift}')
        
w = Worker('Dogancan Torun', 'Sabah')
w.disp()

e=Employee('Dogan')
print(e.name) 

