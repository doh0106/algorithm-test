import sys 
import heapq
sys.stdin = open('input.txt')
n, m = map(int, sys.stdin.readline().split())
stacks = []
for _ in range(m):
    _ = sys.stdin.readline()
    tmp = list(map(int, sys.stdin.readline().split()))
    stacks.append([-i for i in tmp])
heapq.heapify(stacks)


for _ in range(n):
    target = heapq.heappop(stacks)
    num = -target.pop(0)
    if n==num:
        n-=1
    else:
        print("No")
        sys.exit(0)
    if target:
        heapq.heappush(stacks, target)


print('Yes')
sys.stdin.close()