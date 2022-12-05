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
