# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:23:13 2020

@author: Asus
"""

#Subject:İterable classes and generators&generator expressions


#iterable nesneyi tek tek ele geçiriyorum for kullanmadan nesneyi gezdim
a = [10, 20, 30, 40, 50]

it = a.__iter__() #it=iter(a) aynı anlama geliyor bu satırla
x = it.__next__()
print(x)
x = it.__next__()
print(x)
x = it.__next__()
print(x)
x = it.__next__()
print(x)
x = it.__next__()
print(x)

#yukardaki kodun dunder kullanmadan yazımı 
a = [10, 20, 30, 40, 50]

it = iter(a)
x = next(it)
print(x)

x = next(it)
print(x)

x = next(it)
print(x)

x = next(it)
print(x)

#stop_iteration kullanımı 
a = [10, 20, 30, 40, 50]

it = iter(a)   # a.__iter__()

try:
    while True:
        val = next(it)  # it.__next__()
        print(val)
except StopIteration:
    pass
### random sayıları dolaşılabilir sınıf ile yaptım
import random

class Rand:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        val = random.randint(self.a, self.b)
        self.count += 1
        return val
    
r = Rand(0, 99, 10)
result = list(r)
print(result)

#iteretor sınıfının kullanımı 
import random

class Rand:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        
    def __iter__(self):
        return RandIterator(self.a, self.b, self.n)
    
class RandIterator:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.count = 0
        
    def __next__(self):
     if self.count == self.n:
         raise StopIteration
     val = random.randint(self.a, self.b)
     self.count += 1
     return val

    
for x in Rand(0, 99, 10):
    print(x, end=' ')

#tersten bir listi tersten  dolaşım 
a = [1, 2, 3, 4, 5]

for x in reversed(a):
    print(x, end=' ')

#kendi yazdığım  sınıfı tersten dolaşma yukardaki işlemin __reversed__ile dolaşma reversed aslında __reversed__ çağırıyor
a = [1, 2, 3, 4, 5]

for x in a.__reversed__():
    print(x, end=' ') 

#reversed_iterator_ozelliği 
class myrange:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError()

        if stop == None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i == self.stop:
            raise StopIteration()
        self.i += self.step
        return self.i - 1


        
for i in myrange(10):
    print(i)

## 
class myrange:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError()

        if stop == None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        self.i = self.start
        return self
    
    def __reversed__(self):
        return myrange_reverse_iterator(self.start, self.stop, self.step)
            
    def __next__(self):
        if self.i == self.stop:
            raise StopIteration()
        self.i += self.step
        return self.i - 1

class myrange_reverse_iterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.i = stop
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.i == 0:
            raise StopIteration
        self.i -= 1
        return self.i
        
for i in myrange(10):
    print(i, end= ' ')
    
for i in reversed(myrange(10)):
    print(i, end= ' ')

#generator field kullanımı
def foo():
    print('ok')
    yield 100
    
for i in foo():
    print(i)

#yield ornekelri 
def genrange(n):
    for i in range(n):
        yield i   #sürekli yield yazan yerde duracak
        
g = genrange(10)
a = list(g)
print(a)

#yield orneği 
def foo():
    yield "ali"
    yield "veli"
    yield "selami"
    
for s in foo():
    print(s)
    
#yieldın arasına return koyup kestim 

def foo():
    yield "ali"
    yield "veli"
    return  #returnün kesmesiyle selamiyi basamadım
    yield "selami"
    
for s in foo():
    print(s)

#generator kullanmadan asal sayıları bulan kod 
def isprime(val):
    if val % 2 == 0:
        return val == 2
    
    for i in range(3, int(val ** 0.5), 2):
        if val % i == 0:
            return False
    return True
        
def getprimes(n):
    result = []
    for i in range(2, n):
        if isprime(i):
            result.append(i)
            
    return result
            
    
a = getprimes(100)  
print(a)

#Yukardakı ornegın generatorlu halı:
#Burada degısen sey, tum asalları lısteye doldurmak yerıne bız ıstedıgımızde verdı,
#yine asal sayı elde ettık boylecene gereksız buıyuk bır lıste vermedı.  
#Bir fonk bıze bir seyı lısteye  doldurup vermekle generateor ıle vermek arasında arka tarafta bellek acısından lıste olusturmadan bız ıstedıgımız zaman bıze gerı verdı.
def isprime(val):
    if val % 2 == 0:
        return val == 2
    
    for i in range(3, int(val ** 0.5), 2):
        if val % i == 0:
            return False
    return True
        
def getprimes(n):
    for i in range(2, n):
        if isprime(i):
            yield i
    
g = getprimes(100)  
for i in getprimes(100):
    print(i, end= ' ')
#Ornek
def myrange(start, stop = None, step = 1):
    if step == 0:
        raise ValueError('step must not be 0!')
    
    if stop == None:
        stop = start
        start = 0
        
    i = start
    while i < stop:
        yield i
        i += 1
        
        
for i in myrange(10):
    print(i, end=' ')


#Ornek:
def getrand(a, b, n):
    import random
    
    result = []
    for i in range(n):
        val = random.randint(a, b)
        result.append(val)
        
    return result

a = getrand(0, 1000000, 1000)
print(a)

#iterable bir nesne yardımıyla çiftleri alıyorum (liste atamıyorum yield kullanıyorum)
def geteven(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x

l = [2, 5, 7, 8, 4]
for i in geteven(l):
    print(i, end=' ')
print()  

#Tuple compherensıon diye nitelendirebilir
#Sentaks tamamen tuple compherantıongıbıdır.
#Her calıstıgında yield yapılarak duruyor gıbı dusun.
#Bunu dolastıgımızda her defasında bır ıterasyonda duruyor ve sonra devam ediyor.
#Ornek:
g = (i * i for i in range(10)) #generator objem

x = list(g)
print(x)

#Buradan elde ettıgımız sey bir generator objecttir. Yukardakının tamamen esdegerı:
def temp():
    for i in range(10):
        yield i * i

g = temp()
x = list(g)
print(x)  

 



