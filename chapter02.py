# 2장 함수 만들기
# 함수 생성 기준: 반환값, 전달인자값
# 1. 전달 인자가 없는 형태
def greet():
    print("반갑습니다. 임우성님")
    print("Hello~ Python world")

greet()
# run을 시키면 위의 greet가 실행된다.
# 이 메모장 같은 workspace와 idle workspace를 번갈아가면서 이용이 가능하다.

def MH():
    print("1+2+3+4+5 = ", 1+2+3+4+5)
    print("Simple is the best!!!")
    print("행복한 파이썬")

MH()

# 2. 전달 인자가 있는 형태
def greet2(name):
    print("반갑습니다.", name+"님")
    print("Hello~ Python world")

greet2("임우성")

def greet2(name):
    print("반갑습니다.", name+"님")
    print("Hello~ Python world")

greet2("hyun")

def adder(num1, num2):
    print("덧셈 결과 = ", num1+num2)

adder(100,50)

# 연습문제2-2
def multi_string(str):
    print("반갑습니다.", str+"님")
    print("Hello~ Python world", str)
    print("문자열 3번 출력: ", str)

multi_string("hyun")

#2
def conversion_arguments(num):
    print(num*(-1))

conversion_arguments(-32)
conversion_arguments(32)
conversion_arguments(-7)

#3
def adder_divide(num1, num2):
    print((num1 + num2) / 2)

adder_divide(3, 4)

# 함수만들기3: 값의 반환이 존재하는 것

def adder2(num1, num2):
    ar = num1+num2
    return ar

result = adder2(3,4)
print(result)

def add(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def main():
    print(add(5,3))
    print(min(5,3))
    print(mul(5,3))
    print(div(5,3))

main()


