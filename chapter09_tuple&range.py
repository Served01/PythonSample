# tuple 자료형
# 값의 변화(추가나 수정)가 자주 발생하면 리스트 자료형을 씁니다.
# 반대이면, 그렇지 않으면 튜블형(고정된 데이터만 사용)을 사용합니다.
# 왜? 튜플은 값의 변경이 안됩니다.
# 처음 만들어진 상태 그대로 사용해야 합니다.
# 튜플 : ( )
# t1 = ()
# t2 = (10, )
# t3 = (10, 20, 30)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
#del t1[2]
#TypeError: 'tuple' object doesn't support item deletion

t1 = (1, 2, 'a', 'b')
#t1[0] = 'c'
#TypeError: 'tuple' object does not support item assignment

#1.indexing
t1 = (1, 2, 'a', 'b')
print(t1[0]) # 1
print(t1[3]) # 'b'
print(type(t1)) # <class 'tuple'>

#2.slicing
t1 = (1, 2, 'a', 'b')
print(t1[1:]) # (2, 'a', 'b')

#3.tuple 더하기
t2 = (30,40)
print(t1 + t2) # (1, 2, 'a', 'b', 30, 40)

#4.tuple 곱하기
print(t2 * 3) # (30, 40, 30, 40, 30, 40)

#5.길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1)) # 4

#아래의 string형과 list형 으로부터 tuple형을 생성하세요.
str_red = 'Red'
list_color = ['Red', 'Yellow', 'Pink']

tuple_Red = ('R', 'e', 'd')
tuple_color = ('Red', 'Yellow', 'Pink')

tuple_Red2 = str_red
tuple_color2 = tuple(list_color)

print(tuple_Red2) # Red
print(tuple_color) # ('Red', 'Yellow', 'Pink')
print(tuple_color2) # ('Red', 'Yellow', 'Pink')

#어떤 고등학교에서 평소에 영어, 수학, 과학, 사회 4과목을
#시험을 봅니다. 하지만 올해에는 수학 과목을 과제로 대체하려고
#합니다. 이때, 수학 과목만 과제로 대체한 리스트를 출력하는
#프로그램을 작성합니다. 단, 원래 과목 목록은 변하지 않습니다.

a=70
c=80
d=85
sub=('영어','수학','과학','사회')
exam=list(sub)
exam[1]='과제'

print(exam)

# 요구사항
#어느 문구점에서 연필은 200원, 펜은 800원, 지우개는 500원,
# 자는 300원으로 판매를 합니다.
# 이 목록을 list 형태로 만들어 보세요.

items=['연필','펜','지우개','자']
price=[200,800,500,300]
print(items)
print(price)

tuple_1 = tuple(items)
tuple_2 = tuple(price)
print(tuple_1)
print(tuple_2)

print("\n")
#연습문제 9-1

#ds = (1, 2, 3)
#ds = to_list(ds)
#ds
#[1, 2, 3]

#ds = "hello"
#ds = to_list(ds)
#ds
#['h', 'e', 'l', 'l', 'o']

ds = (1, 2, 3)

def to_list(t):
    st = []
    for i in t:
        st.append(i)
    return st
dt = to_list(ds)
print(dt)
print("\n")
#ds
#[1, 2, 3]

#ds
#['h', 'e', 'l', 'l', 'o']

#연습문제 09-2
#문제1)
for i in range(9, 0, -1):
    print(7 * i, end = ' ') # 63 56 49 42 35 28 21 14 7
print("\n")

#문제2)
tp = tuple(range(1, 100, 1)) + tuple(range(100, 0, -1))
print(tp)

#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
# 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
# 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
# 97, 98, 99, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85,
# 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66,
# 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47,
# 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28,
# 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9,
# 8, 7, 6, 5, 4, 3, 2, 1)




























