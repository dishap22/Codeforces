def isBeautiful(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    gc = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            gc += 1

    if gc == 1 and arr[-1] > arr[0]:
        return False
    elif gc <= 1:
        return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    c = input().split()
    s = ''
    for j in range(n):
        arr.append(c[j])
        if isBeautiful(arr):
            s += '1'
        else:
            s += '0'
            arr.pop()
    print(s)