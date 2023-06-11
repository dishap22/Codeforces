num = int(input())
count = 0
for i in range(num):
    val = input()
    if val.find('+') != -1:
        count += 1
    elif val.find('-') != -1:
        count -= 1
print(count)