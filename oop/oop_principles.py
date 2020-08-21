# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:16:30 2020

@author: Dogancan Torun
"""

#subject:Encapsulation-overloading-polymorphism 

#pythonda overloading yok türemiş sınıfın metodu taban sınıfın metodunu eziyor  
class A:
    def foo(self):
        print('A.foo')
        
class B(A):
    def foo(self):
        print('B.foo')
        
b = B()
b.foo()

#veya alternatif olarak asagıdakı ıkısı yerıne A.foo(b) kullanılabılır:
a = A()
a.foo()

#Başka örnek 
class A:
    def foo(self):
        print('A.foo')
        
class B(A):
    def foo(self):
        #A.foo(self)
        super(B, self).foo()
        print('B.foo')
        

b = B() #b nesnesini oluşturur oluşturmaz __init__ ile A'nın foosunu çağırıyor
b.foo() 

#-super()'i parametresız method ıcınde kulanırız dısarıda kullanmayız ama parametlrelı halini  method dısında kullanabıolırız.
class A:
    def foo(self):
        print('A.foo')
        
class B(A):
    def foo(self):
        print('B.foo')
        

b = B()
super(B, b).foo() 

#Taban ve turemıs Sınıflarda Aynı Isımlı Ornek Oznıtelıklerı
#Yanı taban ve turemıs sınıf aynı ısımlı instace attrıbute ıcerebılıyır(java, c++ gibi prog dillerinde)
#-Pythonda boyle bır sey yoktur.
#Python'da üstüne yazıyor gibi dusunmelısın. Yani en son hangısı calısmıssa en sonda o degeri goruruz  

class A: 
    def __init__(self): 
        self.x=10 

class B(A): 
    def __init__(self):  
        super(B,self).__init__() 
        self.x=20 

b=B() 
print(b.x) #b sınının x attribute a yı ezdi 

#Encapsulation : 

#Method kapsülleme örneği: 
class Sample:
    def do_something_important(self):
        #....
        self._foo() #bu methodlar kapsüllenmiş
        #....
        self._bar() #bu methodlar kapsüllenmiş
        #....
        self._tar() #bu methodlar kapsüllenmiş
        #....

    def _foo(self): #bu methodlar kapsüllenmiş
        pass

    def _bar(self): #bu methodlar kapsüllenmiş
        pass

    def _tar(self): #bu methodlar kapsüllenmiş
        pass

s = Sample()
s.do_something_important() 

#Örnek özniteliklerinde kapsülleme örneği 
class Sample:
    def __init__(self, a, b):
        self._a = a  #örnek özniteliğini kapsülledim
        self._b = b


s = Sample(10, 20)
print(s._a, s._b)

#double underscore ile kapsülleme derecesi artar ve dışarıdan erişim zorlaşır 
class Sample:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b


s = Sample(10, 20)
print(s.__a, s.__b)    #erişemem hata alırım
print(s._Sample__a)   # ==>Erismek istersek dısarıdan bu sentaksla kullanacaz

#-Yukarıdakı ornegın erısebılmek ıcın asagıdakı gıbı yazmalıyız kodu
class Sample:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

s = Sample(10, 20)
print(s._Sample__a, s._Sample__b) 

#-Cift __ lu methoda dısarıdan erısme ornegı
class Sample:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __foo(self):
        print('should not be user outside')

s = Sample(10, 20)
s._Sample__foo() 

#Polimorphism:Farklı nesnelerın temelde ıslemlerı farklı yaptıkları halde aynı ısımlı benzer ıslerı yapan methodların olması ve bu methodlar yolu ıle turden bagımsız kod parcalarının olması cokbicimciliktir.


#Bir ornek;

#birşeyi play ile çaldırmak istersek her sınıf içinde play methodu bulundurmalı
def play_music(p): #aldıgı nesnenin türünü bilmeden fonkda kullanıyor
    p.play()
    
class MP3:
    def __init__(self, file):
        self.file = file

    def play(self):
        print(self.file + ' dosyası çalıyor')

mp3 = MP3('shelovesyou.mp3')
play_music(mp3) #mp3 nesnesini play_music methoduna verdik ve play methodu mp3 çaldı

class MPeg4:
    def __init__(self, file):
        self.file = file

    def play(self):
        print(self.file + ' dosyası çalıyor')

mp4 = MPeg4('mozart.mpeg4')
play_music(mp4) #mp4 nesnesini play_music methoduna verdik ve play methodu mp4 çaldı

    
class Wav:
    def __init__(self, file):
        self.file = file

    def play(self):
        print(self.file + ' dosyası çalıyor')

wav = Wav('ding.wav')
play_music(wav) #wav nesnesini play_music methoduna verdik ve play methodu wav çaldı 

#Özet olarak !!Farklı sınıfların birbirlerine benzeyen farklı ısler yapan methodları olacak bu sınıfların, biz de bu metodları dısarıdan kullancaz !!  
 
#__str__:method kullanımı: 
#str(a) = a.__str__() yani bu ıkısı aynı anlamda
#__str__ ==>bu methodun gerı donus degerı bir str olmalı
#Basit bir ornek
class Sample:
    def __str__(self):
        return 'this is a sample object'
    
    
s = Sample()

text = str(s)           # s.__str__()
print(text) #text türü str oldu

#Yanı kendı yazdıgımız sınfıları bir str'ye donusturebılırız.
x=123
s=x.__str__() #bu ifade cast işleminin aynısı
print(s) 


#__str__ ornek2:Kendi sınıfımın __str__ siyazıldı
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    
d = Date(10, 12, 2003)

print(d)








