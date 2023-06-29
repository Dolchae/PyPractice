a,b = input().split()
c = input()
a = int(a)
a *= 60
b = int(b)
c = int(c)
time = a+b+c
hour = time//60
if hour >= 24:
    i = hour//24
    hour -= 24*i
min = time%60

print(hour,min)
