import sys 
import heapq
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
first_word = sys.stdin.readline().strip()
# print(first_word)jjj
target = []
word_len =len(first_word)

for c in first_word:
    # print(c)
    target.append(c)

# print(target)


for _ in range(n-1):
    word = sys.stdin.readline().strip() 
    for idx in range(word_len):
        if target[idx] == '?':
            continue
        if word[idx]==target[idx]:
            continue
        else:
            target[idx] = '?'
# print(target)
        




    # print(word)
print(''.join(target))

sys.stdin.close()