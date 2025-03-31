import sys 
from collections import deque 
sys.stdin = open('input.txt')
n, m = map(int, sys.stdin.readline().split())
# print(n, m)
s = set()
for _ in range(n):
    word = sys.stdin.readline().strip()
    # print(word)
    # s.ad
    for i in range(1, len(word)+1):
        s.add(word[:i])
    # print([word[:i] for i in range(1, len(word)+1)])
# print(s)
answer = 0
for _ in range(m):
    target = sys.stdin.readline().strip()
    if target in s:
        answer += 1
print(answer)

    

sys.stdin.close()