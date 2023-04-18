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
aList = [[['#' for i in range(4)] for j in range(3)] for k in range(5)]
print(aList)
