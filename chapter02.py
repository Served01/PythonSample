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
