n = int(input())
for i in range(n):
    stir = input()
    if len(stir) > 10:
        print(stir[0]+str((len(stir)-2))+stir[-1])
    else:
        print(stir)