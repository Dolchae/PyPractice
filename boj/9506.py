n = int(input())
total = 0
alist = []
while(n != -1):
    for i in range(1,n):
        if n%i == 0:
            alist.append(i)
            total += i
    if total == n:
        print(n,"= ",end="")
        for i in range(len(alist)-1):
            print(f"{alist[i]} + ",end="")
        print(f"{alist[i+1]}")
    else:
        print(f"{n} is NOT perfect.")

    n = int(input())
    total=0
    alist = []
