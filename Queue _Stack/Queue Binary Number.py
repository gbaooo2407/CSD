from collections import deque

def enter(n):
    n = int(input())

def solution(n):
    queue = deque()
    queue.append(1)

    res = 0
    while len(queue) > 0:
        cur = queue[0]
        queue.popleft()
        if cur <= n:
            res += 1

            queue.append(cur * 10)
            queue.append(cur * 10 + 1)

    print(res)

if __name__ == '__main__':
    n = 0

    enter(n)
    solution(n)