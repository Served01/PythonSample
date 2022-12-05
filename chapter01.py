Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 33+55
88
>>> 45+90
135
>>> 
>>> 
>>> 
>>> a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> dd
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dd
NameError: name 'dd' is not defined. Did you mean: 'id'?
>>> DD
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    DD
NameError: name 'DD' is not defined
>>> AB+BC
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    AB+BC
NameError: name 'AB' is not defined
>>> 33+55=44+0
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 33+44==44+0
False
>>> print("Hello, world!")
Hello, world!
