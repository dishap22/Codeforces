n, k = map(int, input().split())
arr = []
arr = input().split()
arr2 = [None] * n

for i in range(n):
    arr2[i] = int(arr[i])

arr2.sort(reverse=True)
count = 0
val = arr2[k-1]

for i in range(n):
    if arr2[i] > 0 and arr2[i] >= val:
        count += 1

print(count)