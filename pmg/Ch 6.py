'''
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

