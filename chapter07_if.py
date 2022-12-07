#7장 조건문

r = 3 < 10
print(r)

print(type(r)) # <class 'bool'>

def main():

    num = int(input("정수 입력 : "))

    if num > 0:
        print("양의 정수 입니다.")

    else:
         print("음의 정수 입니다.")   

main()


def main2():

    num = int(input("정수 입력 : "))

    if num > 0:
        print("0보다 큰 양의 정수 입니다.")
    elif num < 0:
        print("0보다 작은 음의 정수 입니다.")
    else:
        print("0입니다.")

main2()


# equlas() : 참조변수 일 경우 비교, *내용을 
#  ==     : 기본자료형 일 때 비교, 내용을 


def positive():

    num = int(input("정수 입력 : "))

    if num > 0:
        print("0보다 큰 양의 정수 입니다.")
    elif num < 0:
        print("0보다 작은 음의 정수 입니다.")
    else:
        print("0입니다.")

def adder(num1, num2):
    print(num1 + num2)

def main():
    positive()
    adder(5, 3)

main()


#Quiz) 영어단어 문제를 출제하기 위하여 아래와 같은
# 단어가 준비되어 있습니다.
# ex1 = ["risk", "issue", "test", "maintenance", "mat"]
# ex2 = ["security", "pain", "design", "system", "safe"]
# ex3 = ["maintenance", "verification", "validation"]

# 위의 3가지의 list중에서 하나를 골라서.
# 영어 단어 시험을 출제 합니다.
# 1."maintenance"라는 단어를 이용합니다.
# 2. 영어 단어의 갯수는 적어도 5개는 되어야 합니다.

# 시험 문제로 사용할 수 있는 리스트를 찾아서
# 프로그램을 작성해 보세요.

ex1 = ["risk", "issue", "test", "maintenance", "mat"]
ex2 = ["security", "pain", "design", "system", "safe"]
ex3 = ["maintenance", "verification", "validation"]

if('maintenance' in ex1) and (len(ex1) >= 5):
    print('ex1을 시험 출제로 사용합니다.')
elif('maintenance' in ex2) and (len(ex2) >= 5):
    print('ex2를 시험 출제로 사용합니다.')
elif('maintenance' in ex3) and (len(ex3) >= 5):
    print('ex3을 시험 출제로 사용합니다.')
else:
    print('시험 출제로 사용할 데이터가 존재하지 않습니다.')

    # ex1을 시험 출제로 사용합니다.    

#연습문제 7-1

#1.

def RelationOparation():
    num = int(input("정수 입력: "))

    if num >= 0:
        print("입력한 값이 0이거나 0보다 큽니다.")
    else:
        print("입력한 값이 0보다 큽니다.")
    

def main():
    RelationOparation()

main()

#2.
num = 3

print(1 < num and num < 5) # True

#3.
num = 12
print(num < 3 or num > 10) # True

#4.
num = 4
print(num % 2 == 0 and num % 3 != 0) # True


#5.
def RelationOparation2():
    num = int(input("정수 입력: "))

    if num < 0:
        print("입력한 값이 0보다 작습니다.")
    elif 0 <= num < 10 :
        print("입력한 값이 0이상 10미만 입니다.")
    elif 10 <= num < 20:
        print("입력한 값이 10이상 20미만 입니다.")
    else:
        print("입력한 값이 20보다 큽니다.")

def main():
    RelationOparation2()

main()
    

#연습문제 7-2

def RelationOparation3():
    
    num = input("정수 입력: ") # "123"

    if num.isdigit():
        print(int(num) ** 2)
    else:
        print("입력한 값이 정수형이 아닙니다.!!!")

def main():
    RelationOparation3()

main()    

print(bool(0)) # False






      

