Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
33+55
88
45+90
135



a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a
NameError: name 'a' is not defined
dd
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
>>> print(3+5)
8
>>> print('3+5=',3+5)
3+5= 8
>>> print('[문제1] 임우성')
[문제1] 임우성
>>> print('[문제2] 1~10 사이의 결과는 = '. 1+2+3+4+5+6+7+8+9+10)
SyntaxError: invalid syntax
>>> print('[문제2] 1~10 사이의 결과는 = ', 1+2+3+4+5+6+7+8+9+10)
[문제2] 1~10 사이의 결과는 =  55
>>> print('[문제3] 2의 5승을 구하여 출력하세요. 결과는 = ', 2*2*2*2*2)
[문제3] 2의 5승을 구하여 출력하세요. 결과는 =  32
>>> print('[문제4] 5-(3-1)을 구하여 출력하세요. 결과는 = ', 5-(3-1))
[문제4] 5-(3-1)을 구하여 출력하세요. 결과는 =  3
>>> print('[문제5] 5 * 2을 구하여 출력하세요. 결과는 = ', 5*2)
[문제5] 5 * 2을 구하여 출력하세요. 결과는 =  10
>>> print('[문제6] 5 / 2을 구하여 출력하세요. 결과는 = ', 5/2)
[문제6] 5 / 2을 구하여 출력하세요. 결과는 =  2.5
>>> 
>>> v1 = 25
>>> v2 = 30
>>> print(v1+v2)
55
>>> 
>>> x=3*50
>>> y=x+120
>>> print('y의 값은 = ', y)
y의 값은 =  270
>>> 
