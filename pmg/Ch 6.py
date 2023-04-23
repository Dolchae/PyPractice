
#03
mylist = [20,1,12,9,18]

for i in range(len(mylist)):
    for j in range(mylist[i]):
        print("*",end="")
    print()


#09
import turtle
t = turtle.Turtle()
t.shape("classic")
aList = [10,20,30,40,50,60,70,80,90,100,110,120]

for i in aList:
    t.forward(i)
    t.stamp()
    t.backward(i)
    t.right(30)

turtle.mainloop()
turtle.bye()
'


#12        


#13
import random

alist = [['.' for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        n = random.random()
        if n < 0.3:
            alist[i][j] = '#'

for i in range(10):
    print(*alist[i])

#16
s = []
for i in range(2,101):
    s.append(i)

for i in range(2,101):
    if i>=len(s):
        break
    for j in range(i,101):
        if j>=len(s):
            break
        if s[j]%i == 0:
            s.pop(j)
            
 

print(s)


#01.
n = int(input("입력할 값의 개수: "))
alist = []
for i in range(n):
    k = int(input())
    alist.append(k)
print("값의 합계:",sum(alist))


#02.
import random
alist = []
for i in range(10):
    alist.append(random.randint(1,100))
print(alist)


#04.
alist = [i for i in range(1,11)]
print("실행전",alist)
alist = [i*(-1) if 3<=i<=8 else i for i in alist]
print("실행후",alist)


#05.
alist = ['aba','xyz','abc','121']
n=0
for i in alist:
    if i[0]==i[-1]:
        n += 1
print("문자열의 개수=",n)


#06.
alist = [1,2,3,4,5,6]
blist = [6,7,8,9,10]
v = False
for i in range(len(alist)):
    for j in range(len(blist)):
        if alist[i] == blist[j]:
            v = True
            break
print(v)


#07.
import random
alist = []
for i in range(10):
    alist.append('a'+str(i))
print(random.choice(alist))


#08.   ??????
a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]
comlist = [a[i] for i in range(5) for j in range(7) ]

print(comlist)



#10.
import turtle

t = turtle.Turtle()
color = ['yellow','red','purple','blue']

def draw_square(x,y,c):
    for c in color:
        t.draw_square()


#11.
import random
import turtle

die = [1,2,3,4,5,6]
distance = random.choice(die)
print(distance)
one = turtle.Turtle()
one.color('blue')
one.shape('arrow')

two = turtle.Turtle()
two.color('red')
two.shape('turtle')

(distance)
distance = random.choice(die)
print(distance)
two.forward(distance)

turtle.mainloop()
turtle.bye()


#13.
seat = [[0 for _ in range(10)]for _ in range(10)]
done = False
while(done==False):
    for i in range(len(seat)):
        print(*seat[i])

    a = int(input("원하시는 좌석의 행번호를 입력: "))
    if a==-1 or b==-1:
        break
    b = int(input("좌석의 열번호 입력:"))

    if seat[a][b] != 0:
        print("이미 차있는 좌석.")
    else:
        seat[a][b] = 1
        print("예약완료")


#15.
alist = [0,0,0,0,1,0,1,1,1,0]
size = 1
max_size = 0
for i in range(len(alist)-1):
    if alist[i+1]==alist[i]:
        size += 1
    else:
        size = 0
    if size>max_size:
        max_size = size


print("최대길이=",max_size)

