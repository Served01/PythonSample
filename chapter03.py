# 3장 사용자로부터 데이터 입력과 반복 처리

def adder(num1,num2):
    sum = num1+num2
    print(sum)

value1 = input("1숫자를 입력해 주세요.")
value2 = input("2숫자를 입력해 주세요.")

#eval: 수식을 숫자로 변환하여 연산합니다.

num1 = eval(value1)
num2 = eval(value2)

adder(num1, num2)

result = eval(input("수식을 넣어주세요."))
print(result)


# 반복문: for

# List 구조: [  ] 사용
for i in [0, 1, 2]:
    print(i)
    print("Hello~")

for i in [100, 103, 105]:
    print(i)
    print("Hello~")


# [문제3] 구구단에서 7단을 출력하는 코드를 for루프 기반으로 작성
dan = 7
for i in [1,2,3,4,5,6,7,8,9]:
    print(dan, "x", i, "=", dan*i)

# [문제4] 7단을 거꾸로 ...7 x 9 = 63 구하는 코드를 for루프 기반으로 작성
dan = eval(input("구구단을 선택하세요."))

for i in [9,8,7,6,5,4,3,2,1]:
    print(dan, "x", i, "=", dan*i)

#for..in..range

sum = 0
for i in range(1, 11):
    sum=sum+i

print(sum)

# 연습문제 3-4
# 문제1
for i in range(0, 5):
    print("안녕하세요")
    

# 문제2
dan = eval(input("구구단을 선택하세요."))
for i in range(1,10):
    print(dan,"x",i,"=",dan*i)
    

# 문제3
def exp(x,y):

    result = 1
    for i in range(y):
        result = result * x
        print(result)

exp(3,4)


# 문제4
def greet():
    num = eval(input("인사를 몇 번 할까요?"))
    for i in range(num):
        print("반갑습니다.")

greet()

