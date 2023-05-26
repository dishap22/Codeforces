import sys
my_str = sys.stdin.readline()
count = 0

while my_str:
    my_str = sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split()))
    if sum(nums) >= 2: 
        count += 1

sys.stdout.write(count)