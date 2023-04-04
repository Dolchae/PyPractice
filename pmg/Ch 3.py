#chapter 3. 조건문

#01.
x = int(input("정수를 입력하시오: "))
y = int(input("정수를 입력하시오: "))
if x%y==0:
    print("약수입니다.")
else:
    print("약수가 아닙니다.")


#02.
tem = int(input("현재 온도를 입력하시오: "))
if tem >= 25:
    print("반바지를 추천합니다.")
else:
    print("긴바지를 추천합니다.")

#04.
r = int(input("원의 반지름: "))
if r<0:
    print("잘못된 값입니다")
else:
    print("원의 면적: ",r*r*3.14)


#05.
x,y,z = eval(input("3개의 정수를 입력하시오: "))
if x<y:
    min = x
    if min > z:
        min = z
elif y<x:
    min = y
    if min > z:
        min = z
print(f"제일 작은 정수는 {min}입니다.")


#07.
height = int(input("키를 입력하시오(cm): "))
age = int(input("나이를 입력하시오: "))
if height >= 140 and age >= 10:
    print("타도 좋습니다.")
else:
    print("죄송합니다.")


#08.
h,w = input("체중과 키를 입력하시오: ").split(" ")
h = int(h)
w = int(w)

if (h-100)*0.9>w:
    print("저체중입니다.")
elif (h-100)*0.9==w:
    print("표준체중입니다.")
else:
    print("과체중입니다.")


#10.
x = float(input("x의 값을 입력하시오: "))
if x <=0:
    y = x**2 -9*x +2
else:
    y = 7*x +2
print("f(X)의 값은",y)


#11.
w = float(input("무게(킬로그램): "))
h = float(input("키(미터): "))
BMI = w/h**2
print("당신의 BMI:",BMI)
if BMI >=20 and BMI <= 24.9:
    print("정상입니다.")
elif BMI <= 29.9:
    print("과체중입니다.")
elif BMI >= 30:
    print("비만입니다.")


#12.
year = int(input("연도를 입력하시오: "))
if:
pass

#13.
year = int(input("연도를 입력하시오: "))
if ((year%4==0)and(year%100!=0) or year%400==0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")


#15.
n = int(input("정수를 입력하시오: "))
if n%3==0 and n%5==0:
    print("Python Express")
elif n%5==0:
    print("Express")
elif n%3 == 0:
    print("Python")
