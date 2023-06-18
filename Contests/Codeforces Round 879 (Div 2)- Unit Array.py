num = int(input())
for i in range(num):
    l = int(input())
    arr = list(map(int, input().split()))

    negCount = arr.count(-1)
    posCount = arr.count(1)

    count = 0
    while negCount > posCount:
        index = arr.index(-1)
        arr[index] = 1
        negCount -= 1
        posCount += 1
        count += 1

    if negCount % 2 == 1:
        print(1+count)
    else: 
        print(count)
