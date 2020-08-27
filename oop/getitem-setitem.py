# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:01:31 2020

@author: Asus
"""

#getitem-setitem kullanımı


#bazı nesneleri method gibi çağırabiliriz __cal__ ile çağırıyoruz 
class Sample:
    def __call__(self):
        print('__call__ called')
        
s = Sample()
s()     # s.__call__()

#__call__ argüman gönderme 
class Sample:
    def __call__(self, x, y, z):
        print('__call__ called')
        return x + y + z
        
s = Sample()
result = s(10, 20, 30)     
print(result)

#yukaridaki örneğin en genel hali 
class Sample:
    def __call__(self, *args):
        print('__call__ called')
        return sum(args)
        
s = Sample()
result = s(10, 20, 30, 40, 50)     
print(result)

#sınıf nesnesini köşeli parantezle kullanmak istersem getitem ile eşdeğerdir. 
class Sample:
    def __getitem__(self, index):
        print('__getitem__')
        return index * 2
        
s = Sample()

x = s[10]       # s.__getitem(10)
print(x)

#Sınıfımı array gibi kullandım 
class Array:
    def __init__(self, size):
        self.array = [0] * size

    def __getitem__(self, index):
        return self.array[index]


a = Array(10)
x = a[3]        # a.__getitem__(3)
print(x)

#getitem-setitem örnek  
class Array:
    def __init__(self, size):
        self.array = [0] * size
        
    def __getitem__(self, index):
        return self.array[index]
    
    def __setitem__(self, index, val):
        self.array[index] = val
        
s = Array(10)
for i in range(10):
    s[i] = i
    
for i in range(10):
    print(s[i], end=' ')



#tarih sanki bir diziymiş gibi belli bir elemanını alıp kullanıyorum 
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    def __getitem__(self, index):
        if index < 0 or index > 2:
            raise IndexError('out of range')
        if index == 0:
            return self.day
        if index == 1:
            return self.month
        return self.year
    

d = Date(10, 12, 2009)
print(d)
day = d[0]
print(day)
month = d[1]
print(month)
year = d[2]
print(year)




#Setitem örnek: 
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    def __getitem__(self, index):
        if index < 0 or index > 2:
            raise IndexError('out of range')
        if index == 0:
            return self.day
        if index == 1:
            return self.month
        return self.year
    
    def __setitem__(self, index, val):
        if index < 0 or index > 2:
            raise IndexError('out of range')
        if index == 0:
            self.day = val
        elif index == 1:
            self.month = val
        else:
            self.year = val

d = Date(10, 12, 2009)

print(d)
d[0] = 20
print(d) 


#karma örnek: 
class Sample:
    def __init__(self):
        self.dict = {}
        
    def __setitem__(self, key, value):
        self.dict[key] = value
        
    def __getitem__(self, key):
        return self.dict[key]
    
    
s = Sample()
s['ali'] = 300
s['veli'] = 200
s[100] = 'kazım'

print(s['ali'])
print(s['veli'])
print(s[100]) 



#matrix ekrana basma örneği 
class Matrix:
    def __init__(self, nrows, ncols):
        self.matrix = [[0] * ncols for i in range(nrows)]

    def __getitem__(self, index):
        return self.matrix[index[0]][index[1]]

    def __setitem__(self, index, val):
        self.matrix[index[0]][index[1]] = val

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if k != 0:
                    s += ' '
                s += str(self.matrix[i][k])
            s += '\n'

        return s

m = Matrix(5, 5)

for i in range(5):
    for k in range(5):
        m[i, k] = i + k

for i in range(5):
    for k in range(5):
        print(m[i, k], end=' ')
    print()
    
print()
print(m) #str şeklinde ekrana basıyor  

#kendi yazdığımız sınıfta slicing işlemi yapma örneği 
#slice built in sınıfıyla bunu yapabiliriz 
#slice nesnesi oluşturup içinden istediğimizi çekebiliyoruz 

class Sample:
    def __int__(self):
        return 100
    
s = Sample()
x = int(s)  # s.__int__()
print(x)


#Math operations by my class
import math
class Rational:
    def __init__(self, a, b = 1):
        self.a = a
        self.b = b

        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

        self.simplify()

    def simplify(self):
        result = math.gcd(abs(self.a), abs(self.b))
        self.a //= result
        self.b //= result

    def __str__(self):
        if self.b == 0:
            raise ValueError('invalid rational number!')
        if self.b == 1:
            return str(self.a)
        if self.a == 0:
            return '0'
        return f'{self.a}/{self.b}'

    def __add__(self, r):
        num = self.a * r.b + self.b * r.a
        denom = self.b * r.b
        return Rational(num, denom)

    def __sub__(self, r):
        num = self.a * r.b - self.b * r.a
        denom = self.b * r.b
        return Rational(num, denom)

    def __mul__(self, r):
        num = self.a * r.a
        denom = self.b * r.b
        return Rational(num, denom)

    def __truediv__(self, r):
        num = self.a * r.b
        denom = self.b * r.a
        return Rational(num, denom)

    def __pow__(self, x):
        num = self.a ** x
        denom = self.b ** x
        return Rational(num, denom)

    def __lt__(self, r):
        return self.a / self.b < r.a / r.b

    def __le__(self, r):
        return self.a / self.b <= r.a / r.b

    def __gt__(self, r):
        return self.a / self.b > r.a / r.b

    def __ge__(self, r):
        return self.a / self.b >= r.a / r.b

    def __eq__(self, r):
        return self.a / self.b == r.a / r.b

    def __ne__(self, r):
        return self.a / self.b != r.a / r.b

    def __neg__(self):
        return Rational(-self.a, self.b)

    def __pos__(self):
        return Rational(self.a, self.b)
    
    def __float__(self):
        return self.a / self.b
        

r = Rational(2, 3)
f = float(r)
print(f)
        