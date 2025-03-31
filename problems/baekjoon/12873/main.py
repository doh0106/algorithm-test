import sys 
from collections import deque 
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())

people = [i for i in range(n)]
# print(people)
idx = 0
num = 1
# print('asdf')

while len(people) > 1:
    go = num**3 - 1
    num += 1
    print('go', go)
    idx = (idx + go) %len(people)  
    print('before', people, idx)
    people.pop(idx)
    if idx >= len(people):
        print('minus')
        # idx -= 1
        idx = 0
    print('after', people, idx)
    # idx = min(idx, len(people)-1)
    # print(idx)
    print()
    # break
print(people[0]+1)

    

sys.stdin.close()