'''


#03
def calc(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
ans = calc(x,y)
a,b,c,d = ans
print(f"{a}, {b}, {c}, {d}이 반환되었습니다.")

#06.
import random
def MathQuestion(n1,n2):
    r = random.choice('+-/*')
    s = "합은?"
    if r == '-':
        s = "차는?"
    elif r == '/':
        s = "값은?"
    elif r == '*':
        s = "곱은?"
    print(f"정수 {n1}{r}{n2}의 {s}")

a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번재 정수를 입력하시오: "))
MathQuestion(a,b)


#10
def testPrime(n):
    if n==2:
        return 1
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1

for j in range(2,101):
    if testPrime(j)==1:
        print(j,end=" ")


#13.
import random
def dice_game():
    print("======= dice_game() 호출 =======")
    human = int(input("인간: 주사위값= "))
    computer = random.randint(1,6)
    print("컴퓨터: 주사위값=",computer)
    if human>computer:
        print("인간승리")
    elif human==computer:
        print("무승부")
    else:
        print("컴퓨터승리")
    print("======= dice_game() 복귀 =======")

while True:
    s = input("중단할까요? ")
    if s == 'Y':
        break
    else:
        dice_game()

import turtle


#15.
def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size += 5

t = turtle.Turtle()
t.shape("turtle")
for i in range(0,220,20):
    draw_square(i)
turtle.mainloop()
turtle.bye()
'''


#01.
def get_peri(r=5.0):
    print(3.14*2*r)

get_peri()

#05.
def checkPass(p):
    s,l,d = 0,0,0
    for i in p:
        if i.isupper()==True:
            s = 1
        if i.islower()==True:
            l = 1
        if i.isdigit()==True:
            d = 1
    if s==True and d==True and l==True:
        print("완료")
    else:
        print("다시 만드시오")

checkPass('asdkD8')


#09.
a = int(input())
b = int(input())

for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

#11.
def deci2bin(n):
    alist = []
    i=n
    while(i>=1):
        if i%2==0:
            alist.append(0)
        else:
            alist.append(1)
        i = i//2

    for i in range(len(alist)-1,-1,-1):
        print(alist[i],end="")

n = int(input("10진수"))
deci2bin(n)

import turtle


#16.
def draw_line():
    turtle.forward(100)
    turtle.backward(100)
for i in range(10):
    draw_line()
    turtle.right(36)
