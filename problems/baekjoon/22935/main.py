import sys 

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
nums = list(range(1, 16)) + list(range(14, 1, -1))
# nums
bin_nums = [bin(i)[2:] for i in nums]
bin_nums = [i.zfill(4) for i in bin_nums]
bin_nums = [i.replace('1', '딸기').replace('0', 'V') for i in bin_nums]
for _ in range(n):
    t = int(sys.stdin.readline())-1
    print(bin_nums[t%len(bin_nums)])


sys.stdin.close()