# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:39:33 2020

@author: Dogancan Torun
"""

#Subject:OOP fundamentals:Multi inheritance 


#-Bir sınıfı hıcbır sınıftan turetmemıssek aslında onun buılt-in bıcımde kendılıgınden object sınıfından turetıldıgı anlamına gelır. Object buılt-in bir sınıftır.  
#Pythonda tum sınıflar enınde sonunda object sınıfından turetilmiştir.
#-Asagıdakı ıkı tanesı aynı anlamda yanı

Class Sample:
	pass
	
Class Sample(object):
	pass 

#mro(member resolution order)
#Elimizde X sınıfının türetildiği sınıfları bulmak için kullanılır(Türetme hiyerarşisini verir)
#mro bize bir tuple verir. 
    
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__mro__) 

#--------------------------------------------------------------------------------------

#Python Multi İnheritance(Coklu Kalıtım)  
#-Pythonda coklu turetme parantezler ıcerısıne birden fazla sınıfın virgullerle ayrılarak yazılmasıyla olusturulur.

class A:
    pass

class B:
    pass

class C(A, B):
    pass
print(C.__mro__)  

#Burada eger ki class C(B, A): yapsaydık sonuc:
#(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>) seklınde cıkardı. Yani turemısten tabana dogru bu sekılde ilerliyor gibi dusun.

#multi inheritance örnek 
class A:
    def foo(self):
        print('A.foo')

class B:
    def bar(self):
        print('B.bar')

class C(A, B):
    def tar(self):
        print('C.tar')

c = C();

c.foo()
c.bar()
c.tar()


#Multi İnheritance __init__ kullanımı 2 şekilde aşağıdaki gibi yapabiliriz

#1)taban sınıfın __init__ metodunu keyword kullanmadan çağırmak 
class A:
    def __init__(self, a):
        self.a = a
        
    def foo(self):
        print('A.foo')

class B:
    def __init__(self, b):
        self.b = b
        
    def bar(self):
        print('B.bar')

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c
        
    def tar(self):
        print('C.tar')

c = C(10, 20, 30);

print(c.a, c.b, c.c)

#2)__init__ metodunu super keywordu ile çağırma  

#Super fonksiyonunun icine sınıf ısmı veriyoruz. Sonra nesne referansı verıyoruz(self).==> super(C, self).__init__()==>
#Super methodu .dan sonra mro sırasına gore ilgili  taban fonksyionun __init__  methodunu otomatık olarak cagırır. 

class A:
    def __init__(self):
        print('A.__init__')
    
class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')
    
class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')

#Burada D'den sonra B sınıfı geldıgı ıcın burada super(D, self).__init__() B sınıfının __init__methodu , sonra da C'ninki , sonra da A'nın kı cagırlır
class D(B, C):
    def __init__(self):
        super(D, self).__init__() #superde mro sırasına göre D den sonra B yi çağırıyor
        print('D.__init__')
        
d = D() 

#Not:Super fonksıyonu argumanlı veya argumansız seklınde kullanılabılır. Her ıkısı de aynı ısı yapıyor.  
#Argumansızı daha pratık ama  argumanlı daha acık ve guzel.

#argümansız super kullanımı

# super().__init__() ==>Biz hangı sınıfta bulunuyorsak o sınıftan mro sınıfına gore bir sonrakı sınıfıın __init__ methodunu cagır demek bu.  
#Yani hangi sınıfın ıcerısınde hangı taban sınıfın __init__ methodunu cagıracagını kendısı ayıkıyor
class A:
    def __init__(self):
        print('A.__init__')
    
class B(A):
    def __init__(self):
        super().__init__()
        print('B.__init__')
    
class C(A):
    def __init__(self):
        super().__init__()
        print('C.__init__')
        
class D(B, C):
    def __init__(self):
        super().__init__()      # super(D, self).__init__()
        print('D.__init__')
        
d = D() 


#MRO sırası karısık örnek1: 
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')

class D(B):
    def __init__(self):
        super(D, self).__init__()
        print('D.__init__')

class E(D, C):
    def __init__(self):
        super(E, self).__init__()
        print('E.__init__')

e = E()

#MRO sırası karısık örnek2 
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')

class D(B, C):
    def __init__(self):
        super(D, self).__init__()
        print('D.__init__')

class E(D):
    def __init__(self):
        super(E, self).__init__()
        print('E.__init__')

class F(D):
    def __init__(self):
        super(F, self).__init__()
        print('F.__init__')

class G(E, F):
    def __init__(self):
        super(G, self).__init__()
        print('G.__init__')

print(G.__mro__)

g = G()

#MRO karısık örnek 2 nin 2.cevabı 
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        #A.__init__(self)
        super().__init__()
        print('B.__init__')

class C(A):
    def __init__(self):
        super().__init__()
        print('C.__init__')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class E(D):
    def __init__(self):
        super().__init__()
        print('E.__init__')

class F(D):
    def __init__(self):
        super().__init__()
        print('F.__init__')

class G(E, F):
    def __init__(self):
        super().__init__()
        print('G.__init__')

print(G.__mro__)

g = G()


#-Yukarıdakı ornegın argumansız kullanımı
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        #A.__init__(self)
        super().__init__()
        print('B.__init__')

class C(A):
    def __init__(self):
        super().__init__()
        print('C.__init__')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D.__init__')

class E(D):
    def __init__(self):
        super().__init__()
        print('E.__init__')

class F(D):
    def __init__(self):
        super().__init__()
        print('F.__init__')

class G(E, F):
    def __init__(self):
        super().__init__()
        print('G.__init__')

print(G.__mro__)

g = G()




#---------------------------------------------------------------------------------------- 

