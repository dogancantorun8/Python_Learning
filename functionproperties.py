# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:22:31 2020

@author: Dogancan Torun
"""


#Subject:Functions Properties(* , ** arguments   and calling) 

#default argument assignee
def foo(a, b = 10, c = 20):
    print(f'a = {a}, b = {b}, c = {c}')
    
foo(100)        # foo(100, 20, 30)
foo(100, 200)   # foo(100, 200, 30)
foo(100, 200, 300)  #def foo(a,b=10,c) is not declared

#if we always need same messages you will find this function
def disp_msg(msg = 'ok'):
    print(msg)
    
disp_msg()  

#this function need two parameters  
def banner(text, char='-'):
    print(char * len(text))
    print(text)
    print(char * len(text))
    
    
banner('mike')
banner('mike', '*') 

#patterns with stars 
def disp_chars(n, ch = '*'):
    for i in range(1, n + 1):
        print(ch * i)
        
        
disp_chars(10)
disp_chars(10, '?') 

###################Function Calling Properties #############################
print("*****Function calling properties outputs*****") 

#parameter undepend order
def foo(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
foo(c=100, b=200, a=300) 

#manuel range function creating
def disprange(start, stop = None, step = 1):
    if stop == None:
        stop = start
        start = 0
        
    for i in range(start, stop, step):
        print(i, end= ' ')
    print()
    
disprange(1,10,2)    

#myprint using
def myprint(*args):     #args = ('ali', 'veli', 'selami')
    print(*args)        # print('ali', 'veli', 'selami')    
    

d = {'kevin': 10, 'prince': 20, 'boateng': 30}

myprint(*d)

#simple assigne all parameters 
def foo(a, b = 10, c = 20, d = 30, e = 40, f = 50):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}')
    
foo(100, f=200) 

#single star(*) parameter utilize function definition 
def foo(a, b, *c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    
foo(10, 20, 30, 40, 50)
foo(10, 20, 'atiba', 30, 'elneny', 40.2) 

#give iterable object this function 
def mysum(*a):
    total = 0
    for i in a:
        total += i
        
    return total

t = mysum(10, 20, 30)
print(t)

t = mysum(10, 20, 30, 40, 50) #tuple olarak geçiriliyor 
print(t) 

#* calling string  
def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))
    
    
t = (30, 40, 50, 60)
foo(10, 20, *t)     # foo(10, 20, 30, 40, 50, 60) 
foo(*'samsun')      # foo('s', 'a', 'm', 's', 'u', 'n') 



#give iterable object this function example 2 
def foo(a, b, *c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    
foo(10, 20)   

#give iterable object this function example 3
def foo(a, b, *c, d, e):
    print('a = {}, b = {}, c = {}, d = {}, e = {}'.format(a, b, c, d, e))
    
foo(10, 20, 30, 40, 50, e=1000, d=2000) 

#last two members printing tuple 
def foo(a, b, c, d, e, f, *g):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}, g = {}'.format(a, b, c, d, e, f, g))
    
    
t = (30, 40, 50, 60, 70, 80) 
foo(10, 20, *t) 



print("*************Double stars ouputs********")

#if you not define any argument you will use this two star syntax **
def foo(a, b, **c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    
foo(10, 20, x=100, y=200) 

#double star syntax  dict slicing 
def foo(a, b, **c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    for key, val in c.items():
        print('{} ---> {}'.format(key, val))
        
    
foo(10, 20, vida=100, ruiz=200, diaby=300)     

#double star sen dict 
def foo(a, b, c, **d):
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))
    
d = {'d': 100, 'e': 'barcelona', 'flag': 23.6}
foo(10, 20, 30, **d)   

#reverse print example with double stars
def revprint(*a, **b):
    print(*reversed(a), **b)

revprint(10, 20, 30, 40, 50, sep=',')  

#examples: 
def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))

foo(10, e=50, *(30, 40), **{'d':100, 'f': 200}) 

def foo(a, b, c, d, e, f):
    print('a = {}, b = {}, c = {}, d = {}, e = {}, f = {}'.format(a, b, c, d, e, f))

foo(10, 20, *([40]), **{'d':100}, **{'e':200, 'f': 300})   

#isinstance => check type of arguments
def disp_banner(s): #123 cast etti
    if not isinstance(s, str):
        s = str(s)
    print('-' * len(s))
    print(s)
    print('-' * len(s))
    
disp_banner('steve')
disp_banner(123)


########################  Nested Functions ###########################

#Nested functions: 
def foo():
    x = 10
    def bar():
        print('bar')
        def tar():
            print('tar')
        tar()
            
    print(x)
    bar()
    
foo()
#global function using nested function: 
def foo():
    x = 10
    def bar():
        x = 20
        print(x)
    bar()
    print(x)
        
        
foo()

#if you want to use none-local variable you will write this syntax: 
def foo():
    a = 10    
    def bar():
        nonlocal a
        a = 20
    bar()
    print(a)
    
foo()

#nonelocal variable be careful !
def foo():
    def bar():
        nonlocal a
        a = 10
    a = 0   #this assignee operations is not working 
    bar()
    print(a)
        
foo()

#same names function calling 
def bar():
    print('global bar')
    
def foo():
    def bar():
        print("bar in foo is calling")
    bar()
    
foo()

#nested functions example 
def bar():
    print('global bar')
    
def foo():
    global bar
    bar()
    def bar():
        print("bar in foo is calling")
    bar()
    
foo()
bar()

#Nested function return example
def foo():
    def bar():
        print("bar in foo is calling")
    return bar #retun bar adress

#foo() #if we call this syntax interpreter show error
f = foo() #print bar in foo function 
f()

#globals local function using
x = 10
y = 20

def foo():
    print('foo')

g = globals()

val = g['x']
print(val)

val = g['y']
print(val)

val = g['foo']
print(val)














