t = int(input())

for i in range(0,t):
     score = 0
     count = 0
     a = input()
     for j in range(len(a)):
          if a[j]=="O":
               count += 1
               score += count
          else:
               count = 0
     print(score)
