  
PI = 3.14     # 원주율

#def ar_circle(rad):     # 원의 넓이를 계산해서 반환하는 함수
#    return rad * rad * PI 

#def ci_circle(rad):     # 원의 둘레를 계산해서 반환하는 함수
#    return rad * 2 * PI

def ar_circle(rad):     # 원의 넓이를 출력
    print("넓이: ", rad * rad * 3.14) 

def ci_circle(rad):     # 원의 둘레를 출력
    print("둘레: ", rad * 2 * 3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)

main()


from circle import ar_circle as ac
from circle import ci_circle as cc

def ar_circle(rad):     # 원의 넓이를 출력
    print("넓이: ", rad * rad * 3.14) 

def ci_circle(rad):     # 원의 둘레를 출력
    print("둘레: ", rad * 2 * 3.14)

def main():
    r = float(input("반지름 입력: "))
    ar_circle(r)
    ci_circle(r)

    sum = ac(r) + cc(r)
    print("넓이와 둘레의 합: ", sum)

main()



import circle

def main():
    r = float(input("반지름 입력: "))
    ar = circle.ar_circle(r)
    print("넓이:", ar)
    ci = circle.ci_circle(r)
    print("둘레:", ci)

main()

from circle import ar_circle
from circle import ci_circle

# from circle import ar_circle, ci_circle

def main():
    r = float(input("반지름 입력: "))
    ar = ar_circle(r)
    print("넓이:", ar)
    ci = ci_circle(r)
    print("둘레:", ci)

main()

import circle as cc

def main():
    r = float(input("반지름 입력: "))
    ar = cc.ar_circle(r)
    print("넓이:", ar)
    ci = cc.ci_circle(r)
    print("둘레:", ci)

main()

