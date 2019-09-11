Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Python27/Saad_Ajay/005_dict/001_rep.py =============
{12: 'C', -12.34: [1, 3, 4], (1, 23): set([1, 2, 3])}
<type 'dict'>
58283144
>>> var
{12: 'C', -12.34: [1, 3, 4], (1, 23): set([1, 2, 3])}
>>> var[0]

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    var[0]
KeyError: 0
>>> var[(1,23)]
set([1, 2, 3])
>>> var[123] = "123"
>>> var
{123: '123', 12: 'C', -12.34: [1, 3, 4], (1, 23): set([1, 2, 3])}
>>> var[-12.34]
[1, 3, 4]
>>> var[-12.34] = "hello"
>>> var
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> var
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> b = var.copy()
>>> b
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> var
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> b.clear()
>>> b
{}
>>> var
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> b = var
>>> b
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> var
{123: '123', 12: 'C', -12.34: 'hello', (1, 23): set([1, 2, 3])}
>>> b.clear()
>>> b
{}
>>> var
{}
>>> a = {12:"soc" , 89:"soft"}
>>> b = {89:"new", 123: "soc"}
>>> a.update(b)
>>> a
{89: 'new', 123: 'soc', 12: 'soc'}
>>> a.get(123)
'soc'
>>> a
{89: 'new', 123: 'soc', 12: 'soc'}
>>> var.pop(123)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    var.pop(123)
KeyError: 123
>>> var
{}
>>> a
{89: 'new', 123: 'soc', 12: 'soc'}
>>> a.pop()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> a.pop(123)
'soc'
>>> a
{89: 'new', 12: 'soc'}
>>> a.popitem()
(89, 'new')
>>> a
{12: 'soc'}
>>> #copy , clear, update, pop, popitem, get
>>> a = {12 : "so" , 56:"soft", 78:"45"}
>>> a.keys()
[56, 12, 78]
>>> a.values()
['soft', 'so', '45']
>>> a.items()
[(56, 'soft'), (12, 'so'), (78, '45')]
>>> a
{56: 'soft', 12: 'so', 78: '45'}
>>> a = (123,12)
>>> b = {a : "soc" , a :"soft"}
>>> a
(123, 12)
>>> b
{(123, 12): 'soft'}
>>> #python introduction
>>> #python basic syntax (variable , datatype, keyword, identifiers)
>>> #python built-in fucntions
>>> #python str
>>> #print list
>>> #print tuple
>>> #print set
>>> #print dict
>>> ################# python operators ############
>>> ################# python control statements ###
>>> #################python fuunctions ############
>>> #####################  python 50%  ############
>>> 
