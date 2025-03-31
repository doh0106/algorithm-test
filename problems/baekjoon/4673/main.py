import sys 

sys.stdin = open('input.txt')
is_self = [True for i in range(10001)]

is_self[1] = True
tmp = []
def make_self_num(num):
    # print(num)
    ans = num
    while num>=10:
        a = num%10
        # print(num, a)
        ans += a
        num //= 10
        # print('after', num)
    # print(ans, num)
    ans += num
    return ans
        

for i in range(1, 10001):
    # if i<112:
        # continue
    self_num = make_self_num(i)
    # print(i, self_num)
    if self_num<=10000:
        # print(i)
        is_self[self_num] = False
        # break
    # print(self_num)
for idx, tf in enumerate(is_self):
    if idx == 0:
        continue
    if tf:
        print(idx)




sys.stdin.close()