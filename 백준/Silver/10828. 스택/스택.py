import sys

input = sys.stdin.readline
n = int(input())
stack = []
cmd_list = ['push', 'pop', 'size', 'empty', 'top']

for i in range(n):
    s = list(map(str,input().split()))
    if s[0] == cmd_list[0]:
        stack.append(int(s[1]))
    elif s[0] == cmd_list[1]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif s[0] == cmd_list[2]:
        print(len(stack))
    elif s[0] == cmd_list[3]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == cmd_list[4]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])