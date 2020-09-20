# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:06:24 2020

@author: Dogancan Torun
"""


#subject:Exception 

#try catch kodu bunu debugger ile denemeliyim 
def bar(a):
    print('bar begins')

    [1, 2, 3, 4, 5][a] = 100

    print('bar ends')

def foo(a):
    print('foo begins')

    bar(a)

    print('foo ends')

a = int(input('Bir sayı giriniz:'))

try:
    foo(a)
except ValueError:
    print('ValeError occured')
except IndexError:
    print('IndexError occurred')

print('ends...')

#try catch blogu örnek 
try:
    a = int(input('Bir sayı giriniz:'))
    print(a * a)
except ValueError:
    print('Sayının formatı bozuk!')

print('son')

#value error  -raise kullanımı
#
def foo(a):
    print('foo begins')

    if a < 0:
        raise ValueError()

    print(a ** 0.5)

    print('foo ends')

try:
    val = int(input('Bir değer giriniz:'))
    foo(val)
except ValueError:
    print('ValueError occurred!')

print('Ok')

#banner ile kod kullanımı
def banner(s):
    print('-' * len(s))
    print(s)
    print('-' * len(s))


try:
    banner('ali')
except TypeError:
    print('girilen değer yanlış')

#fonksiyon ile exception fırlatma
# -------------------------------------------

class Rational:
    def __init__(self, a, b):
        self.a = a
        if b == 0:
            raise ValueError()
        self.b = b

    def __str__(self):
        return f'{self.a}/{self.b}'

try:
    x = Rational(3, 0)
    print(x)
except ValueError:
    print('Geçersiz rasyonel sayı!')

# anagram kontrol kodu
def is_anagram(s, k):
    if len(s) != len(k):
        return False

    return set(s) == set(k) #sete attım mükerrerler ortadan kalkıyor


result = is_anagram('halil', 'hilal')
print(result)

#kendi exceptionlarımı oluşturabilirim 
class MyException(Exception): #exception ata sınıfından kendi exception sınıfımı türettim
    pass

def foo(a):
    if a < 0:
        raise MyException

try:
    foo(-1) #foo fonksiyonuna -1 değerini verdim ve exception oluşturdum
except MyException:
    print('MyException oluştu')

print('son')

#kendi exception kodum gelişmiş örnek 
class MyException(Exception):
    pass

class YourException(Exception):
    pass

def foo(a):
    if a < 0:
        raise MyException
    if a == 0:
        raise YourException

try:
    foo(0)
except MyException:
    print('MyException oluştu')
except YourException:
    print('YourException oluştu')

print('son')


#-Birden fazla exception o ya da bu olursa calıssın seklınde kullanabılırız. except(MyException, YourException, …) gibi kullanırız. Icerısıne yazdıgımız exceptıonları sırasının hıcbır onemı de yoktur.
#-Burada exceptlerı () kullancaz, yanı tuple sentaksı ıle kullanıyoruz ama burada dıkkat etmemız gereken sey de ()'siz kullanmadan olmuyor.
class MyException(Exception):
    pass

class YourException(Exception):
    pass

def foo(a):
    if a < 0:
        raise MyException
    if a == 0:
        raise YourException

try:
    foo(0)
except (MyException, YourException):
    print('MyException ya da YourException oluştu')

print('son')

#parametresiz except bloğu özel bir except olarak adlandırılır 
#-Ozel bır excepte vardır. O da parametresız except blogu. Eger kı except'in yanına hıcbır sey yazmazsak bu her seyı tarayıp yakalar demektir.  Makul kodda bu parametresız exceptin exceptlerın en altında olanıdır. Bu zorunludur aslında biz eger ki parametresızı parametrelılerın usttunde yazarsak kod hata verıyor.
class MyException(Exception):
    pass

class YourException(Exception):
    pass

def foo(a):
    if a < 0:
        raise MyException
    if a == 0:
        raise YourException

try: 
    foo(0)
except MyException:
    print('MyException oluştu')
except: #diğer exception oluştu
    print('diğer exception oluştu')

print('son') 


#-try'ın ıcerısıne raise ile exceptıon attık, akıs bırden fazla try blogu ıcerısıne gırıyor(Akıs birden fazla kez try bloguna gırmısken exception olusursa icten dısa dogru taranır). Yanı son girilenden ılk gırılene dogru try blokları taranır:
#Eger ki try ıcerısınde exception olusursa ictekı try'ın exceptıon'una bakılır once, eger ki try'ı except blogu ıctekı exceptı yakalayamazsa dısatakı try'ın exceptıon'u yakalar.
#Yani negatıf deger gırdıgımızda once ıctekı try'ın exceptıne bakılacak, sonra dıstakıne bakılıyor
#OZETLE:
#-İç içe programın akısı bırden fazla try bloguna gırmısken oralarda exceptıon olusmus olabılır. Tryların except blokları ıcten dısa dogru taranmaktadır
#-Onemli Bir Ornek(ormal, negatif, bir de gecersiz bir deger gırerek kodu anlayabiliriz:
class MyException(Exception):
    pass

def foo():
    print('foo başladı')
    try:
        val = int(input('Bir değer giriniz:'))
        if val < 0:
            raise MyException
    except ValueError:
        print('ValueError oluştu')

    print('foo bitti')

try:
    foo()
except MyException:
    print('MyException oluştu')

print('son')

#-Yukarıdakı ornegın ıctekı exceptıon'ı parametresız kullanımı, artık ne alırsa alsın tüm exceptionları ic blok yakalar.
class MyException(Exception):
    pass

def foo():
    print('foo başladı')
    try:
        val = int(input('Bir değer giriniz:'))
        if val < 0:
            raise MyException
    except: 
        print('ValueError oluştu')

    print('foo bitti')


try:
    foo()
except MyException:
    print('MyException oluştu')

print('son') 

#Exception Nesnelerinin Anlamı
#-Bir exception olustugnda bazen exception'un turunu bılmek yeterlı olmuyor, olusan hatalara aıt bır takım ayrıntılara da ıhtıyacımız olabılıyor bazen. Bir exception'u raise yapan kısım bır takım bılgılerı bır sınıf nesnesıne dolduruyor. Yanı sadece exception olustuugunu anlamak degıl de olusan exceptıon hakkında bazı bılgıler elde etmek de onemldır.
#-Bir exception nesnesini almak istersek as degisken_ismi seklinde kullanmalıyız.
#-except icerisine birden fazla tur yazıyorsak eger ki as ile kullanamayız. As ifadesini tek tur icin soyleybılırız.
#-Parametresiz except kullanırsak o exceptten bir nesne yaratamayız.

class MyException(Exception):
    def __init__(self,msg,errcode):
        self.msg=msg
        self.errcode=errcode
    def __str__(self):
        return f"Error: {self.msg}, Code:{self.errcode}"
def foo(a):
    if a<0:
        raise MyException("Value must not be negative",234)
try:
    a=int(input("Bir değer girinz: "))
    foo(a)
except MyException as me:
    print(me)

#Finally Blogu
#Eger kı fınally blogu olacaksa tum exceptlerden sonra gelmelı yanı onların hepsının altında bulunmalıdıır bu blok.
#Finally blogu exception olusmasa da olussa da mutlaka calısır.
#Finaly bolumu try blogundan herhangı bır bicimde cıkıldıgında calıstırılır. Yanı try blogundan her ne sebeple cıkıyor olursak olalım finaly blogu calısır muhakkak. Fonksiyon ıcerısınde breakle cıksak veya return ıle fonksıyuonu sonlandırsak veya continue kullansak dahı finally blogu her turlu calısır. 
#Basit bir ornek:
try:
    a = int(input('Bir değer giriniz:'))
    print(a * a)
except ValueError as ve:
    print(ve)
finally:
    print('finally')





# with Deyimi
# -with ifade as degisken_adi ==>ifade sınıf turunden olacak ve bu da baglam yonetım protokolune uygun olması gerekıyordu.
# -with deyımı finally ye cok benzer. Garantılı bosaltım yapmak ıcın kullanılan bır deyımdır.
# -Genel olarak zaten __del__ methodları bosaltım yapıyor garbage collectorler yanı.
# -BYP(Baglam Yonetım Protokolu) ==>İki tane methodun bulunması gerekmektedir. __enter__ ve __exit__. __enter__'ın sadece self parametresı olacak.
# __exit__'in ise 3 parametresı mevcuttur ve bunlar genellıkle exc_type, exc_value, traceback'dir.
# -exc_type ==>exception olusmamıssa one degerını alır, olusmussa olusan exception sınıf turunu  alır.
# -exc_value==>Olusan exception nesnesi
# -traceback==>Akıs buraya nasıl gelmıs.
# with ornek
class Sample:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


with Sample() as s:
    pass


# -Yukardakı ornegın parametrelerını de yazdırdıgımız halı:
class Sample:
    def __enter__(self):
        print('__enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ called:', exc_type, exc_value, traceback)


with Sample() as s:
    print('with suite')



