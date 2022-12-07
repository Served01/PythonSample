#5장 List와 문자열

print(type([1,2,3])) # <class 'list'>

a = [10, 11, 12, 13, 14, 15]
print(type(a)) # <class 'list'>

#list는 여러 종류의 데이터를 묶어서 표현가능 합니다.
aa = [100, "hello", 33.123]
print(aa)

aaa = [100, 200, [300, 400], ["AAA", "ZZZ"]]
print(aaa)

# Indexing Operation
b = [1,2,3] + [4,5] # [1, 2, 3, 4, 5]
print(b)

bb = [1,2,3] * 5
print(bb)

# [ ] : Indexing Operation
# [  :  ] : Slicing Oparation

st = [1, 2, 3, 4, 5]
n1 = st[0] # 1
n2 = st[4] # 5
print(n1, n2)

st = [1, 2, 3, 4, 5]
st[0] = 500 # 500저장 
st[4] = 100 # 100저장 
print(st) # [500, 2, 3, 4, 100]

print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])

print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])
print(st[-5]) ## [100, 4, 3, 2, 500]

#연습문제 5-1
#[문제1]
st = [11, 12, 13, 14]
print(st[0])
print(st[1])
print(st[2])
print(st[3])

#[문제2]
st = [11, 12, 13, 14]
print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])

#[문제3]
st = [11, 12, 13, 14]
st[0] += 1
st[1] += 1
st[2] += 1
st[3] += 1

print(st)

#방안1
print(st[0] + 1)
print(st[1] + 1)
print(st[2] + 1)
print(st[3] + 1)

#[문제4]

st = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for i in range(10):

    st[i] += 1

print(st) # [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]

#[문제5]

st = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]
st[0], st[-1] = st[-1], st[0]
print(st)

#Example

x = [1, 2, 3, ['a', 'b', 'c']]

# x[0] = 1
# x[1] = 2
# x[2] = 3
# x[3] = a,b,c
# x[3][0] = a
# x[3][1] = b
# x[3][2] = c

print('firstData : ', x[0])
print('secondData : ', x[1])
print('thirdData : ', x[2])
print('forthData : ', x[3])
print('x[3][0] = ', x[3][0])
print('x[3][0] = ', x[3][1])
print('x[3][0] = ', x[3][2])
print('x[-1][0] = ', x[-1][0])
print('x[-1][1] = ', x[-1][1])
print('x[-1][2] = ', x[-1][2])

# 3차원 배열 
#      [0]         [1]                [2]
x2 = [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x2) # [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x2[0])
print(x2[1])
print(x2[2])
#print(x2[0][0]) #[표현불가]
#print(x2[0][0][0]) #[표현불가]

print(x2[3][0])
print(x2[3][1]) 
print(x2[3][2]) 

# 3차원 배열 출력 
print(x2[3][3][0])
print(x2[3][3][1]) 
print(x2[3][3][2]) 

#Slicing 연산

# [  :  ] =>  : 범위지정 연산자 

# python은 열 중심 언어
#[0] 
#[1]
#[2]

#[0][0]
#[1][0]
#[2][0]

#[0][0][0]
#[1][0][0]
#[2][0][0]

# indexing
#     [0]  [1]                                       [9]
st1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
st2 = st1[2:5]
print(st2) #  300, 400, 500

st1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

st1[2:5] = [0, 0, 0, 0, 0]

print(st1) #  [100, 200, 0, 0, 0, 0, 0, 600, 700, 800, 900, 1000]
#데이터의 부분수정 

x = [10, 20, 30, 40, 50]
print(x[0:2]) # [10, 20]

x2 = "12345"
print(x2[0:2]) # 12

x3 = [11, 12, 13, 14, 15]
x4 = x3[ :2] # [11, 12]
x5 = x3[2: ] # [13, 14, 15]

print(x4) 
print(x5) 

x6 = [1, 2, 3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x6[2: ]) # [3, ['a', 'b', 'c', ['hyun', 'kim', 'park']]]

print(x6[3][ :3]) # ['a', 'b', 'c']
# print(x6[3: ][0][ :3])

print(x6[3][3][ :3]) # ['hyun', 'kim', 'park']


#연습문제 5-2

#1.
st = [1,2,3,4,5]
st[1] = []
st[3] = []

print(st) # [1, [], 3, [], 5]

st[1:4] = [3]
print(st) # [1, 3, 5]

#2.
st = [1,2,3,4,5]

st[2:3] = [3, 3.5]
#st[2:4] = [3, 3.5, 4]
print(st) # [1, 2, 3, 3.5, 4, 5]

#3.
st = [1,2,3,4,5]

st[1:4] = []
print(st) # [1, 5]

#4.
st = [1,2,3,4,5]

st[0:5] = []
# st[ : ] = []

print(st) #[]

#5.
st = [1,2,3,4,5,6,7,8,9,10]

nt = st[ : :2]
# nt = st[0:9:2]

print(nt) # [1, 3, 5, 7, 9]

#6.
st = [1,2,3,4,5,6,7,8,9,10]

nt = st[1: :2]
# nt = st[1:9:2]

print(nt) # [2, 4, 6, 8, 10]


#Exercise
x = [10, 20, 30]
y = [40, 50, 60]

print(type(x)) # <class 'list'>
print(type(y)) # <class 'list'>

# + 연산의 결과는 ?
print(x + y) 


# 2차원 배열(2x3) 형태로 출력하여 저장된 결과를 확인해 주세요.
z = [x, y]

print(type(z)) # <class 'list'>

print(z[0][0])
print(z[1][0])
print(z[0][1])
print(z[1][1])
print(z[0][2])
print(z[1][2])

#연습문제 5-3
str = "hello"
str += "python"

print(str) # hellopython

#연습문제 5-4

#문제1>
def sum_all(str):

    sum = 0
    for i in range(len(str)):
        sum += str[i]
    return sum
    
sum = sum_all([1,2,3,4,5])
print(sum) # 15


#문제2>
def show_reverse(str):

    for i in range(len(str)):
        print(str[(i+1) * -1], end = '')

x = show_reverse([1,2,3,4,5])

print(x) # 54321

def show_reverse2(str):

    for i in range(len(str)):
        print(str[(i+1) * -1], end = '')

x2 = show_reverse2("ABCDEFG")

print(x2) # GFEDCBA

st = [1,2,4]
st.insert(2, 3)
print(st) # [1, 2, 3, 4]

st.clear()
print(st) # []

#연습문제 6-2

#1.
str = "The Espresso Spirit"

print(str.upper())
print(str.lower())
print(str)

#2.

def birth_only(pn):

    birth = pn.split("-")
    return birth[0]

p1 = "070609-2011xxx"
p1 = birth_only(p1)
print(p1) # 070609

p2 = "090716-1012xxx"
p2 = birth_only(p2)
print(p2) # 090716





































