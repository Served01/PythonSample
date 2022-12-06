# 5장 List와 문자열

# 데이터상으로 150 같은 숫자는 '스칼라'라고 한다.

# 데이터상으로 [150]을 '벡터'라고 한다.

# 벡터가 여러개 모인 것을 '데이터 프레임'이라고 한다. [10:1], [10,2] 이런 형태들이다.

# 용어상으로 배열이란 말을 잘 안 쓴다.

print(type([1,2,3]))
print(type([1]))

a=[10, 11, 12, 13, 14, 15]
print(type(a))

# list는 여러 종류의 데이터를 묶어서 표현 가능합니다.
aa=[100, "hello", 33.123]
print(aa)

aaa=[100, 200, [300, 400], ["AAA", "ZZZ"]]
print(aaa)

# Indexing Operation
b=[1,2,3] + [4,5]
print(b)

# 이 workspace에서 작업 하는 것을 습관화해라. IDLE은 결국 프로그램을 종료하면 날아가는 데이터이기 때문에 저장을 할 수 있는
# 형태로 하는 것이 좋다.

bb=[1,2,3]*2
print(bb)

# [ ]: Indexing Operation
# [ : ]: Slicing Operation

st=[1,2,3,4,5]
n1 = st[0]
n2 = st[4]
print(n1,n2)

st=[1,2,3,4,5]
st[0] =500
st[4] =100
print(st)

print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])

print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])
print(st[-5])

# 연습문제 5-1
# [문제1]
st=[11,12,13,14]
print(st[0])
print(st[1])
print(st[2])
print(st[3])

# [문제2]
st=[11,12,13,14]
print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])

# [문제3]
st=[11,12,13,14]
st[0] += 1
st[1] += 1
st[2] += 1
st[3] += 1

print(st)

# 방안1
print(st[0]+1)
print(st[1]+1)
print(st[2]+1)
print(st[3]+1)

# [문제4]
st = [100,200,300,400,500,600,700,800,900,1000]

for i in range(10):
    st[i] += 1

print(st)

# [문제5]
st = [100,200,300,400,500,600,700,800,900,1000]
st[0], st[-1] = st[-1], st[0]
print(st)

# Example
x=[1,2,3,['a','b','c']]

#x[0]=1
#x[1]=2
#x[2]=3
#x[3]=a,b,c
#x[3][0]=a
#x[3][1]=b
#x[3][2]=c

print('FirstData:', x[0])
print('SecondData:', x[1])
print('ThirdData:', x[2])
print('ForthData:', x[3])
print('x[3][0]:', x[3][0])
print('x[3][1]:', x[3][1])
print('x[3][2]:', x[3][2])
print('x[-1][0]:',x[-1][0])
print('x[-1][1]:',x[-1][1])
print('x[-1][2]:',x[-1][2])

# 3차원 배열

x2 = [1,2,3,['a','b','c',['hyun','kim','park']]]

print(x2)
print(x2[0])
print(x2[1])
print(x2[2])
print(x2[3][0])
print(x2[3][1])
print(x2[3][2])
print(x2[3][3][0])
print(x2[3][3][1])
print(x2[3][3][2])

# Slicing 연산

# Python은 열 중심 언어
# [0], [1], [2], ...

# [ : ] => 범위 지정 연산자


st1=[100,200,300,400,500,600,700,800,900,1000]
st2=st1[2:5]

print(st2)

st1=[100,200,300,400,500,600,700,800,900,1000]

st2=st1[2:5]=[0,0,0]

print(st1)

x=[10,20,30,40,50]
print(x[0:2])

x2="12345"
print(x2[0:2])

x3=[11,12,13,14,15]
x4=x3[ :2]
x5=x3[2: ]

print(x4)
print(x5)

x6 = [1,2,3,['a','b','c',['hyun','kim','park']]]

print(x6[2:5])
print(x6[3: ][0][3: ][0][ :2])
# [3: ] 이런 형태의 결과물을 하나의 또다른 배열로 인식하므로 뒤에 [0]을 써 준뒤
# 다시 Slicing 형태를 사용하면 된다.

# 연습문제 5-2

st=[1,2,3,4,5]
st[1:4]=[3]
print(st)

#2.
st=[1,2,3,4,5]
st[2:4]=[3,3.5,4]
#st[2:3]=[3,3.5]

print(st)

#3.
st=[1,2,3,4,5]
st[1:4]=[]

print(st)

#4.
st=[1,2,3,4,5]
st[ :5]=[]

print(st)

#5.
st=[1,2,3,4,5,6,7,8,9,10]
nt=st[0:9:2]
#nt=st[ : :2]

print(nt)

#6.
st=[1,2,3,4,5,6,7,8,9,10]
#nt=st[1:9:2]
nt=st[1: :2]
print(nt)

#Exercise
x=[10,20,30]
y=[40,50,60]

#1.+
z=x+y
print(z)

#2. 2차원 배열 형태로 출력하여 저장된 결과를 확인하라.
z=[x,y]
print(z[0][0])
print(z[1][0])

