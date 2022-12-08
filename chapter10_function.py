#function(함수)

# 예제 1

def p(x,y) :
    result = print('%s 과 %s 의 더한 값은 %s 입니다' %(x,y,x+y) )
    return result

p(3,4)


# 예제 2
#여러개의 입력값을 처리하는 함수 만들기(*x)
def p(*x) :
    hap = 0
    for i in x :
        hap += i
    return('입력하신 숫자의 합은 %s 입니다' %hap)

print( p(1,3,5) )
print( p(2,4,6,8) )


# 예제 3

def add(a, b):
    return a + b # 100 + 200 = 300

a = 100
b = 200
c = add(a, b)
print(c) # 300

d = add(3000, 5000)
print(d) # 8000

#함수의 오버로딩
sum = 0

def add(a, b, c):
    sum = a + b + c
    return sum

e = add(11, 22, 33)
print(e) # 66

#입력값이 없는 함수 유형
def say():
    return 'Hi'

a = say()
print(a) # Hi

#반환이 없는 함수

def add(a, b):
    print(a+b) # 70

add(30,40)

#반환이 있는 함수
def add(a,b):
    return a + b

result = add(30, 40)
print(result) # 70


#반환값이 없는데, 전달인자도 업는 함수
def say():
    print('HI')

say() # HI

def add():
    print(30 + 40)

add() # 70

#매개변수 지정하여 호출하기
def add(a, b):
    return a + b

result = add(a=3, b=7)
print(result) # 10

result = add(b=5, a=7)
print(result) # 12


#여러개의 입력값을 처리하는 함수 만들기
def add_many(*args):
    result = 0

    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result) # 6

result = add_many(10, 20, 30, 40, 50)
print(result) # 150


#연습문제 10-1

for i in range(3):
    print(i + 1, i + 2, i + 3, sep = ', ')

#1, 2, 3
#2, 3, 4
#3, 4, 5

#연습문제 10-2
    
def adder(s):
    for i in range(len(s)):
	    s[i] += 1

#st = [1, 2, 3, 4, 5]
#adder(st)
#st
#[2, 3, 4, 5, 6]





