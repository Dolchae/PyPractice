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
print(f"{a} {b} {c} {d}이 반환되었습니다.")

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
