# 4장 자료형 (정수형과 실수형)
data1 = 2
data2 = 2.4
print("정수형 데이터:",data1)
print("실수형 데이터:",data2)

# 부동소숫점: 지수형 데이터
su = 4.24e+10
print(su)

su2 = 4.24e-10
print(su2)

# 8진수 (2^3) = 8(3비트): -128 ~ 127
octal = 0o177
print(octal)

# 16진수 (2^4) = 16(4비트)
octal = 0x177
print(octal)

print(type(3))
print(type(3.1234))

div1=35/3.5
print("실수형 나눗셈(몫)")
print(div1)

div2=35//3
print("정수형 나눗셈(몫)")
print(div2)

div3=35%3.5
print("실수형 나눗셈(나머지)")
print(div3)

div4=35%3
print("정수형 나눗셈(나머지)")
print(div4)

multi1=2**4
print(multi1)

# int or float로의 형변환

num = 100
num = float(num)
print(num)
print(type(num))

num2 = int(num)
print(num2)
print(type(num2))

# 복합 대입 연산자 가능

# 소괄호: ()
aaa=3+4/2
print(aaa)

bbb=(3+4)/2
print(bbb)



