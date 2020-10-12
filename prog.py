import math



def prime(n):

    q = w = r = t = 0    
    e = 1
    w = 1

    if(n == 1):
        e = 0
        
    if (n%2 == 0):
        w = w + 2
        
    
    for i in range(3, n):
        if (n%i == 0):
            w = w + i
         
          
    
    if(n == w and e != 0):
        return 1

    elif(e == 1):
        return 0
    
    elif(q != w):
        return 0

cases = int(input())

l1 = [1,2]
l1.clear()
y = 0

for x in range(0, cases):
    y = int(input())
    l1.append(y)

for x in range(0, cases):
    if(prime(l1[x]) == 1):
        print("YES")

    elif(prime(l1[x]) == 0):
         print("NO")
