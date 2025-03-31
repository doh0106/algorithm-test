import sys 
from collections import deque 
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
q = deque()
max_num = 0
max_stu = 0

def do(com: str):
    global q, max_num, max_stu
    if com.startswith("1"):
        q.append(int(com[2:]))
    else:
        q.popleft()
    if len(q) > max_num:
        max_num = len(q)
        max_stu = q[-1]
    elif len(q) == max_num:
        max_stu = min(max_stu, q[-1])
    
    # print(q, )
    return

for _ in range(n):
    command = sys.stdin.readline()
    do(command)
# print(q)
print(max_num, max_stu)
    

sys.stdin.close()