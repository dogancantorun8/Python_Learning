# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:59:09 2020

@author: Dogancan Torun
"""


#Operatör methodları ve yaygın dunder methodları

#__str__ örnek:Manuel str ye type cast işlemi yaptım 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})';

pt = Point(3, 2)
s = str(pt)
print(s)
print(pt)


#__rep__ örnek : Anlamadım
class Date:
    def __init__(self, day, month, year): #java construct methodu ile aynı
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    def __repr__(self):
        return f'{self.day}-{self.month}-{self.year}' #string enterpolasyonu

d = Date(10,12,2003)  #d değişkenin type'ı Date şeklinde oluyor...
print(d) 


#Kendi yazdıgımız sınıfların karşılaştırılmasını istersek operatör methodu kullanırız. 
#Sen operator işlemi yapıyorsun ama arka planda method çağrılıyor.  
class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, x):
        result = self.val + x.val
        return Number(result)


a = Number(10);
b = Number(20)

c = a + b  # => eşdeğeri  c = a.__add__(b) iki nesneyi topladım
print(c)

#toplama operandının türüne göre  farklı şekillerde toplama örneği : 
class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, x):
        if isinstance(x, int): #int mi değil mi kontrol ediyoruz
            result = self.val + x
        elif isinstance(x, Number):
            result = self.val + x.val
        else:
            raise TypeError('object type mismatch')

        return Number(result)

a = Number(10)
b = Number(20)


c = a + b  # c = a.__add__(b) number türünden iki nesneyi topladım
print(c)

c = a + 20 # c = a.__add__20 number türünden iki nesneyi topladım
print(c) 

#toplama operandından birden fazla argüman ile toplama 
class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, x):
        if isinstance(x, (int, float)):
            result = self.val + x
        elif isinstance(x, Number):
            result = self.val + x.val
        else:
            raise TypeError('object type mismatch')

        return Number(result) 
    

a = Number(10)
b = Number(20)
c = Number(30)

d = a + b + c + 40  # a.__add__(b).__add__(c).__add__(40)
print(d)

d = a.__add__(b).__add__(c).__add__(40) # "+" operatörünün yaptığı işin metod karşılığı
print(d)

#__sub__ operatör methodu örneği :  
class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, x):
        if isinstance(x, (int, float)): #int ya da float kontrolü yapılıyor
            result = self.val + x
        elif isinstance(x, Number):
            result = self.val + x.val
        else:
            raise TypeError('object type mismatch') #exception oluşturdum

        return Number(result)

    def __sub__(self, x):
        result = self.val - x.val
        return Number(result)
    
    

a = Number(10)
b = Number(5)
c = a - b   # a.__sub__(b)
print(c)

#__mul__örneği  
class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __add__(self, x):
        if isinstance(x, (int, float)):
            result = self.val + x
        elif isinstance(x, Number):
            result = self.val + x.val
        else:
            raise TypeError('object type mismatch')

        return Number(result)

    def __sub__(self, x): #sub operations 
        result = self.val - x.val
        return Number(result)

    def __mul__(self, x): #mul operations 
        result = self.val * x.val
        return Number(result)

a = Number(10)
b = Number(5)
c = Number(10)

d = a + b * c 
print(d)

#kendi rasyonel  sınıf örneğimiz 
class Rational:
    def __init__(self, a, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        if self.a == 0:
            return '0'
        return f'{self.a}/{self.b}'

r = Rational(3, 1)
print(r) 

#obeb kodu 
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 

class Rational:
    def __init__(self, a, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 0:
            raise ValueError('invalid rational number!')
        if self.b == 1:
            return str(self.a)
        if self.a == 0:
            return '0'
        return f'{self.a}/{self.b}'


result = gcd(20, 5)
print(result)


#rasyonel örneğine method eklenmiş versiyonu
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


class Rational:
    def __init__(self, a, b = 1):
        self.a = a
        self.b = b
        
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b
        
        self.simplify()
        
    def simplify(self):
        result = gcd(abs(self.a), abs(self.b))
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
        nom = self.a * r.b + self.b * r.a
        denom = self.b * r.b
        result = Rational(nom, denom)
        
        return result
   
    def __sub__(self, r):
        nom = self.a * r.b - self.b * r.a
        denom = self.b * r.b
        result = Rational(nom, denom)
        
        return result

x = Rational(2, 4)
y = Rational(2, 3)
z = Rational(1, 6)
k = x + y - z
print(k)

#operator methoduyla nesne ile int veya float değeri toplama işlemi

class Sample:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, s):
        if isinstance(s, Sample):
            return Sample(self.a + s.s)
        if isinstance(s, int):
            return Sample(self.a + s)
        
    def __radd__(self, s):
        return self.a + s
        
    def __str__(self):
        return str(self.a)
        
s = Sample(10)
result = s + 10
print(result)

result = 10 + s
print(result)

#operator methodu ornek 2 
class Sample:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, s):
        if isinstance(s, Sample):
            return Sample(self.a + s.s)
        if isinstance(s, int):
            return Sample(self.a + s)
        
    def __radd__(self, a):
        return self.a + a
        
    def __str__(self):
        return str(self.a)
        
a = 10
s = Sample(10)

result = s + a    # s.__add__(a)
print(result)

result = a + s    # s.__radd__(a)
print(result)


