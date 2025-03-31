import sys 

sys.stdin = open('input.txt')
from collections import defaultdict
node_dic = defaultdict(list)
# nodes = {}

n = int(sys.stdin.readline())
node_list =  list(map(int, sys.stdin.readline().split()))
# print(node_list)
root_node = None
for i in range(len(node_list)):
    node = node_list[i]
    if i == 0:
        root_node = node
        if len(node_list) == 1:
            node_dic[node].append(-1)
            # break
    else:
        node_dic[node].append(node_list[i-1])
# print(node_dic)
print(len(node_dic))
for k in range(len(node_dic)):
    if k == root_node:
        print(-1, end=' ')
    else:
        print(node_dic[k][0], end=' ')
    # print(k, node_dic[k])

sys.stdin.close()