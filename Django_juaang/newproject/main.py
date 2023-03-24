dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(n):
        for j in range(n):
            cnt = lst[i][j]
            for k in range(4):
                for q in range(1, p+1):
                    newR = i + dr[k]*q
                    newC = j + dc[k]*q
                    if 0<=newR<n and 0<=newC<n:
                        cnt += lst[newR][newC]
            if cnt > maxV:
                maxV = cnt

    print(f'#{tc} {maxV}')


