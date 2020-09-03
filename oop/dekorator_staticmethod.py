# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:57:49 2020

@author: Dogancan Torun
"""

#subject: garbage collector -sınıfların statik methodları ve sınıf methodları - class methodları & dekoratör


#__del__ cağrılan ornek ve garbage collector kullanımı 
class Sample:
    def __del__(self):
        print('Sample.__del__')
        
s = Sample()
print(1)
k = s
print(2)
m = k
print(3)
s = None
print(4)
k = None
print(5)
m = None
print(6)

#turemiş sınıfta __init__ çağırmak ve __del__ kullanmak  
import math

class Sample:
    def __init__(self):
        print('Sample.__init__')
        
    def __del__(self):
        print('Sample.__del__')
        
    
class Mample(Sample):
    def __init__(self):
        super().__init__() #taban sınıfın __init__cağırdım
        print('Mample.__init__')
        
    def __del__(self):
        print('Mample.__del__')
        super().__del__() #taban sınıfın __del__ methodunu çağırdım
        
      
m = Mample()
m = None
print('ok')  

#bir nesnenin kaç referans gösterdiğini de aşağıdaki anlayabiliriz 
import sys

class Sample:
    pass

k = Sample()
print(sys.getrefcount(k) - 1) #kaç tane referans gösteriğini anlıyoruz

s = k
print(sys.getrefcount(k) - 1)
s = None
print(sys.getrefcount(k) - 1)
k = None

#static method sınıfın selfini kullanmadan sınıf içerisinde yazılan methodlar;
#static methodlar spesifik bir nesnenin öz niteliklerini kullanmıyor.ondan dolayı nesne argümanı olan self parametresi fonksiyon içine yazılmaz 
#static methodu sınıftan nesne yaratmadan kullanmak istersem tercih etmeliyim !!!
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @staticmethod
    def is_leap_year(year): #self argümanı vermedim 
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

result = Date.is_leap_year(2000) #nesne yaratmadım 
print(result)

#static method örneği 
class Sample:
    __count = 0
    def __init__(self):
        Sample.__count += 1
    
    @staticmethod
    def get_count():
        return Sample.__count

a = Sample()
b = Sample()

result = Sample.get_count()
print(result)

#class methodları nadiren karşılaşılır self parametresi bunda da yoktur. 
#class methodların birinci parametresi içinde bulunduğu sınıfın type nesnesi geçiriliyor 
class Sample:
    @classmethod
    def foo(cls, a, b):
        print('foo')
        print(cls)


Sample.foo(10, 20)

s = Sample()
s.foo(10, 20) 

#dekoratörler:callable olan yapılarda kullanılır. 
def foo(f):
   print('foo')
   return f

def bar():
    print('bar')

bar = foo(bar)
bar()

#kodun dekoratörlü eş değeri
def foo(f):
    print('foo')
    return f

@foo
def bar():
    print('bar')

bar()

#içiçe çağırım örneği
def tar():
    print('tar')

def foo(f):
    print('foo')
    return tar


def bar():
    print('bar')

bar = foo(bar)
bar()

#içiçe çağırım 2.örnek 
def foo():
    x = 10
    def bar():
        print('bar', x)
        
    bar()
    
    
foo()

def foo(x):
    def bar():
        print('bar', x)
        
    bar()
    
    
foo(100)

#dekoratörün araya girişini anlatan kod 
def foo(f):
    def bar():
        print('araya girilen kod')
        f()
        
    return bar

@foo #test=foo(test) = dekoratörün eş değeri 
def test():
    print('test')
    
test() #her çağrımda bir kez araya giriliyor
test()
test()

#araya  girme kullanılarak count arttırma  method dekoratörü kullanımı
count = 0
def foo(f):
    def bar():
        global count
        count += 1
        f()
        
    return bar
@foo
def test():
    print('test')
    
test() 
print(count)
test() 
print(count)
test()
test()
test()
print(count)

# dekoratör kullanımı örneği 
class foo:
    def __init__(self, f):
        self.f = f
        
    def __call__(self) :
        print('araya girilen kod')
        self.f()
          
@foo  #sınıfsal dekoratör
def test():
    print('test')
    
test() #önce araya giriyor ardından çağırıyor 
test()
test()
test()
test()

#sınıf dekoratör kullanımı 
def foo(s):
    print('foo')
    
    return s

@foo
class Sample:
    pass

s = Sample() #nesne yaratıldığında foo direk çağrılıyor

#sınıf dekoratör kullanımı örneği 2 
def foo(s):
    
    def bar():
        print('Nesne yaratıldığında araya giren kod')
        return s()
    
    return bar


@foo
class Sample:
    pass

s = Sample()
k = Sample()
m = Sample()

#sınıf dekoratör örnek 
def foo(s):
    
    def bar(*args):
        print('Nesne yaratıldığında araya giren kod')
        return s(*args)
    
    return bar

@foo
class Sample:
    def __init__(self, a, b, c, d):
        print(a, b, c, d)

Sample = foo(Sample)

s = Sample(10, 20, 30, 40)


