#8장 for문과 while
#반복문 : 특정 조건문을 반복적으로 수행하는 경우 발생

#for문

def adder():
    sum = 0

    for i in range(1,11):
        sum = sum + i
    print("sum = ", sum, end = ' ') # 55   

def main():
    adder()

main()

print("-----------------------")
print("\n")

su = [10, 20, 30, 40, 50]
i = len(su)

for idx in range(len(su)):
    i = i - 1
    print(su[i]) # 50 40 30 20 10
print("\n")

add = sum = 0
for i in range(1, 11): # 1 ~ 10
    add = add + 1
    sum+=add
    print(sum) # 55
print("\n")

# gugudan 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
        
# 2 4 6 .... 18
# 9 18 27 ..... 81    
print("\n")

result = [x*y for x in range(2,10)
          for y in range(1, 10)]
print(result) # [2,4,6..........72, 81]
print("\n")

#list내포 사용하기
a = [1,2,3,4,5]
result = []

for num in a:
    result.append(num * 3) # 1*3=3, 2*3=6, 3*3=9, ....

    print(result) #[3, 6, 9, 12, 15]
print("\n")

b = [1,2,3,4,5]
result = [num * 3 for num in a]
print(result) #[3, 6, 9, 12, 15]
print("\n")

c = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 == 0]
print(result) # [6, 12]
print("\n")

#quiz) 숫자를 입력 받아서 1부터 n까지의 합을 구하여 출력해 보세요.
n = int(input('숫자 입력'))

sum = 0

for i in range(1, n+1, 1):

    sum+=i

    print(sum)
print("\n")

x = [(1,2), (30,40), (5,6)]

for (first, last) in x:
    print(first + last)  # 3, 70, 11    

for (f, l) in x:
    print(f + l)  # 3, 70, 11

for (a, b) in x:
    print(a + b)  # 3, 70, 11

print("\n")    
print("-----------------------")
print("\n")

x2 = [(1,2,3), (30,40,50), (5,6,7)]

for (first, second, last) in x2:
    print(first + second + last) # 6, 120, 18

for (a, b, c) in x2:
    print(a + b + c) # 6, 120, 18

print("\n")    
print("-----------------------")
print("\n")

#quiz)리스트에 점수가 입력되어 있습니다.
# 번호순으로 합격자와 불합격자를 출력하는 코드를 완성하세요.
# 처리기준은 70점 이상이면 합격 입니다.
# scores = [98, 75, 63, 23, 82, 99]

scores = [98, 75, 63, 23, 82, 99]

n = 0

for score in scores:
    n+=1

    if score >= 70:
        print(n, '번 학생 합격')
    else:
        print(n, '번 학생 불합격')
print("\n")

#연습문제 8-1
#문제1)
num = 0

while num < 10:
	print(num, end = ' ') # 0 1 2 3 4 5 6 7 8 9
	num = num + 1
print("\n")
print("-----------------------")
print("\n")

#문제2)
num = 9

while num >= 0:
	print(num, end = ' ' ) # 9 8 7 6 5 4 3 2 1 0
	num = num - 1
print("\n")
print("-----------------------")
print("\n")

#문제 3)
num = 0
r = 0

while r != 63:
    num = num + 1
    r = 3 * num / 2	

print(r)

print("\n")
print("-----------------------")
print("\n")

#break

def main():
    i = 1
    sum = 0
    
    while i < 11:
        sum = sum + i        
        i = i + 1

    print("sum =", sum, end = ' ')
    
main()
print("\n")

def main():
    i = 1
    sum = 0    
    while True:
        sum = sum + i
        if sum > 100:
            print(i, "더했을 때의 합", sum, end = ' ')
            break
        i = i + 1

main()
print("\n")

def main():
    i = 0    
    while i < 100:
        print(i, end = ' ')
        i = i + 1
        if i == 20: 
            break 

main()
print("\n")

def main():
    i = 1
    sum = 0    
    while sum <= 100:
        sum = sum + i        
        i = i + 1
    print(i, "더했을 때의 합", sum, end = ' ')

main()
print("\n")



#quiz)양의 정수들의 덧셈을 합니다. 더하고자 하는 수를 입력하고,
#0을 입력하면 종료가 되도록 합니다.
print("덧셈을 하고 싶은 양의 정수를 입력해 주세요. 0을 입력하면 종료합니다.")
print("\n")

sum = num = 0

while(1):
    num = int(input())

    if num == 0:
      break
    else:
     sum+=num

    print("합계 : %d" % sum, "입니다.")
    print("합계 : ", sum, "입니다.")
print("\n")
#덧셈을 하고 싶은 양의 정수를 입력해 주세요. 0을 입력하면 종료합니다.
#10
#합계 : 10 입니다.
#합계 :  10 입니다.
#20
#합계 : 30 입니다.
#합계 :  30 입니다.
#50
#합계 : 80 입니다.
#합계 :  80 입니다.
#0

coffee = 5

while True:
    money = int(input("돈을 입력하세요."))

    if money == 300:
        print("Coffee 판매합니다.")
        coffee = coffee - 1
    elif money > 300:
        print("잔돈 %d을 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 돌려주고 커피를 주지 않습니다")
        print("남은 커피 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("coffee가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print("\n")

# 무한루프 탈출 방법

count = 1
while(True):
    str = "hello2"
    print(str)
    count = count + 1

    if count == 5:
        break

print("\n")


#연습문제 8-2

#https://ko.khanacademy.org/math/cc-sixth-grade-math/cc-6th-factors-and-multiples/cc-6th-lcm/a/least-common-multiple-review
#https://myjamong.tistory.com/138

#최소공배수 LCM(Least Common Multiple)
#최소공배수는 두 자연수의 공통된 배수 중 가장 작은 수를 의미한다.
#최소공배수 = 두 자연수의 곱 / 최대공약수
#ex) 72 와 30의 최소공배수는 360이다.

#문제1)
lcm = 0
n = 45

while True:
    if n % 6 == 0 and n % 45 == 0:
             lcm = n
             break
    n = n + 1
print(n)

print("\n")
#>>> lcm
#90

# 최대공약수 GCD(Greatest Common Divisor)
#최대공약수는 두 자연수의 공통된 약수 중 가장 큰 수를 의미한다.
#ex) 72 와 30의 최대공약수는 6이다.

#문제2)
gcm = 0
n = 42

while True:
    if 42 % n == 0 and 120 % n == 0:
        gcm = n
        break
    n = n - 1    
print(n)

print("\n")
#>>> gcm
#6	

#continue
    
for i in range(1, 11):

    if i % 2 == 0:
        continue
    print(i, end  = ' ') # 1 3 5 7 9

print("\n")

marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number+=1

    if mark < 60:
        continue

    print("%d번 학생 합격을 축하합니다." %number)
    
#1번 학생 합격을 축하합니다.
#3번 학생 합격을 축하합니다.
#5번 학생 합격을 축하합니다.
print("\n")
    
# while문

a = 0
while a < 10:
    a = a + 1

    if a % 2 == 0:
        continue  # 짝수이면 다음 데이터로 넘어 갑니다.

    print(a) # 홀수이면 출력을 합니다.
print("\n")

# 1~ 10가지의 합계를 구하여 출력하세요.
num = sum = 0
while(num <=10):
    sum+=num # 6 = 3 + 3
    num+=1   # 4 = 3 + 1
    
    print(sum) # 0, 1, 3, 6
print("\n")

# 1~ 10까지의 수 중에서 홀수의 합계를 구하여 출력하세요.   
num = 1
sum = 0

while(num <= 10):
    sum+=num
    num+=2

    print(sum) # 1, 4, 9, 16, 25
print("\n")

# hello라는 문자열을 10번 출력하세요.
count = 1
while(count <= 10):
    print("Hello")
    count+=1
print("\n")

count = 1
while(count <= 10):
    str = "hello2"
    print(str)
    count = count + 1
print("\n")






#[연습문제 08-3]

#문제1)
for i in range(1, 10):
    if (7*i) % 2:
        continue
    print(7 * i, end = ' ') # 14 28 42 56


print("\n")
#문제2) 
num = 1

while num < 100:
    num += 1

    if num % 2 == 0 or num % 3 == 0:
	    continue
    print(num, end = ' ')

#5 7 11 13 17 19 23 25 29 31 35 37 41 43 47 49 53 55 59 61 65 67 71 73 77 79 83 85 89 91 95 97
print("\n")
#문제3) 
num = 1

while num < 100:
    num += 1

    if num % 2 != 0 and num % 3 != 0:
	    print(num, end = ' ')

#5 7 11 13 17 19 23 25 29 31 35 37 41 43 47 49 53 55 59 61 65 67 71 73 77 79 83 85 89 91 95 97
print("\n")

#다중 for loop

for i in [1, 2]:
    for j in ['a', 'b', 'c']:
        print(j * i, end = ' ') # a b c aa bb cc
print("\n")

for i in [1, 3]:
    for j in ['a', 'b', 'c', 'd']:
        print(j * i, end = ' ') # a b c d aaa bbb ccc ddd
print("\n")

#연습문제 8-4
        
for i in range(2, 10):
    for j in range(1, 10):
	    print(i * j, end = ' ')
    print('\n', end = ' ')

    
        










        
  
