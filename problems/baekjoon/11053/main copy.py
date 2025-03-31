import sys

sys.stdin = open("input.txt")

stack = []
n = int(sys.stdin.readline())


def do(command: str):
    if command.startswith("push"):
        num = int(command[5:])
        stack.append(num)
        # print("push", stack)
    elif command.startswith("size"):
        print(len(stack))
    elif command.startswith("empty"):
        if not stack:
            print(1)
        else:
            print(0)
        # print()
    elif command.startswith("pop"):
        if not stack:
            print(-1)
        else:
            tmp = stack.pop(len(stack) - 1)
            print(tmp)
            # print("pop", stack)
    elif command.startswith("top"):
        if not stack:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    else:
        raise ValueError()

    return


for _ in range(n):
    command = sys.stdin.readline().strip()
    do(command)
    # print(stack)

sys.stdin.close()
