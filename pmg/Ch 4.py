#Chapter 04
'''
#01.
for i in range(2,51,2):
    print(i,end=" ")


#02.
myList = [11,22,23,99,81,93,35]
sum=0
for i in range(0,len(myList)):
    sum += myList[i]
print(sum)


#03.
sum = 0
for i in range(1,101):
    if i%3==0:
        sum += i
print(f"1 부터 100 사이의 모든 3의 배수의 합은 {sum}입니다.")


#04.
n = int(input("정수를 입력하시오: "))
print("약수:",end=" ")
for i in range (1,n+1):
    if n%i==0:
        print(i,end=" ")


#05.
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")


#06.
import math

print("각도  sin값  cos값")
for i in range(0,91,10):
    print(i," ",math.sin(3.14*i/180.0)," ",math.cos(3.14*i/180.0))


#07
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range


#08.
n=1
while(n*n<500):
    n += 1
print(n)


#09.
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print("\n")


n = int(input("n의 값을 입력하시오: "))
result = 0
for i in range(1,n+1):
    result += i*i
print(result)


a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))
k=1
ans=k
for k in range(1,max(a,b)+1):
    if a%k==0 and b%k==0:
        ans=k

print(f"{a}와 {b}의 최대 공약수는 {ans}입니다.")


n = int(input("몇 번째 항까지 구할까요?"))
a = 0
b = 1
print("0, 1, 1",end=", ")
for i in range(n-2):
    a,b = b,a+b
    print(a+b,end = " ")


#14.
for i in range(2,21):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        print(i,end=" ")


#15.
sum = 0
for i in range(1,100,2):
        sum += i/(i+2)
print(sum)


#16.
size = int(input("게임판의 크기: "))
for j in range(size):
    for i in range(size):
        print("---",end=" ")
    print("\n")
    if j == size-1:
        break
    for i in range(size + 1):
        print("|", end="  ")
    print("\n")

#18.
import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
for i in range(10):
    x = random.randint(-350,350)
    y = random.randint(-350,350)
    r = random.randint(1, 100)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(r)
turtle.mainloop()
'''



