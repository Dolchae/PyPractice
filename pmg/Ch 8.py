#01

class Cat:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name+" "+str(self.__age)

    def setName(self):
        self.__name = name

    def setAge(self):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

missy = Cat('Missy',3)
lucky  = Cat('Lucky',5)
print(missy)
print(lucky)

#02.
class Rocket:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.y)

    def moveUp(self):
        self.y += 1

myRocket = Rocket(0,0)
print("로켓의 높이:",myRocket.y)
myRocket.moveUp()
print("로켓의 높이:",myRocket.y)


#04
class Rectangle:
    def __init__(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return str(self.__x)+str(self.__y)+str(self.__width*self.__height)

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def setwWidth(self,width):
        self.__width = width

    def setHeight(self,height):
        self.__height = height

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getArea(self):
        return (self.__width * self.__height)

    def overlap(self,other):

        if not r1.__x < r2.__x < r1.__x + r1.__width and not \
                r1.__x < r2.__x + r2.__width < r1.__x + r1.__width and not \
                r1.__y < r2.__y < r1.__y + r1.__height and not \
                r1.__y < r1.__y+r1.__height < r1.__y + r1.__height:
            return False
        else:
            return True

r1 = Rectangle(0,0,100,100)
r2 = Rectangle(10,10,100,100)

if r1.overlap(r2) == True:
    print("r1과 r2는 서로 겹칩니다.")

else:
    print("r1과 r2는 서로 겹치지 않습니다.")


#06.
class Person:
    def __init__(self,name,mobile="01234",office="56789",email="a@company.com"):
        self.__name = name
        self.__mobile = mobile
        self.__office = office
        self.__email = email

    def setName(self,name):
        self.__name = name

    def setMobile(self,mobile):
        self.__mobile = mobile

    def setOffice(self,office):
        self.__office = office

    def setEmail(self,email):
        self.__email = email

    def getName(self):
        return self.__name

    def getMobile(self):
        return self.__mobile

    def getOffice(self):
        return self.__office

    def getEmail(self):
        return self.__email

    def __str__(self):
        return "("+self.__name+","+self.__mobile+","+self.__office+","+self.__email+")"

p1 = Person("Kim",office="1234567",email="kim@company.com")
p2 = Person("Park",office = "2345678")
print("p1 = Person",p1)
print("p2 = Person",p2)
p2.setEmail("park@company.com")
print("p2 = Person",p2)


#08.
class printSong:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing(self):
        for i in self.lyrics:
            print(i)

aSong = printSong(["TWINKLE, twinkle, little star","How I wonder what you are!","Up above the world so high,","Like a diamond in the sky."])
aSong.sing()
