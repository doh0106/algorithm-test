import sys

sys.stdin = open("./input.txt", "r")

n = int(sys.stdin.readline())
array_n = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array_m = list(map(int, sys.stdin.readline().split()))

for i in array_m:
    if i in array_n:
        print(1)
    else:
        print(0)

sys.stdin.close()
