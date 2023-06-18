def formula(n1, n2):
    l1 = len(str(n1))
    l2 = len(str(n2))
    if l1 > l2:
        n2.zfill(l1-l2)
    elif l2 > l1:
        n1.zfill(l2-l1)
    
    l1 = len(str(n1))
    sum = 0
    for i in range(l1):
        sum += abs(int(n1[i]) - int(n2[i]))
    return sum
        
 
n = int(input())
for i in range(n):
    b, e = map(int, input().split())
    if b == e:
        print(0)
        continue
    max = e-b
    maxStrength = formula(b, e)
    for i in range(0, max+1):
        for j in range(0, max+1):
            val = formula(str(i), str(j))
            if val > maxStrength:
                maxStrength = val
    print(maxStrength)