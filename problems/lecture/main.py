import sys

sys.stdin = open("input.txt", "rt")
#######################################################
## 1.
# 100000 * 10000 = 10억: n^2 절대 안됨

n, m = map(int, sys.stdin.readline().strip().split(" "))
# print(n, m)
lectures = list(map(int, sys.stdin.readline().strip().split(" ")))
# print(lectures)
# n*log(n) :

left, right = max(lectures), sum(lectures)
# print(left, right)
answers = []


def check(disc):
    count = m
    tmp = disc
    for l in lectures:
        if (tmp - l) < 0:
            tmp = disc
            count -= 1
        if count <= 0:
            return False
        tmp -= l
    if tmp >= 0:
        return True
    return False


while left < right:
    mid = (left + right + 1) // 2
    # print("i", left, mid, right)
    # mid = 15
    is_go = check(mid)
    if is_go:
        answers.append(mid)
        right = mid - 1
    else:
        left = mid
    # print("is go", is_go)
# print(answers)
# print(len(answers))
# print(answers[-10:])
print(min(answers))


#######################################################
sys.stdin.close()
