T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    loc = []

    for k in range(1, 11):
        for i in range(N):
            for j in range(N):
                if lst[i][j] == k:
                    loc.append((i, j))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    row = 0
    col = 0
    d = 0
    cnt = 0

    for i in loc:
        while row != i[0] or col != i[1]:
            row = row + dr[d]
            col = col + dc[d]
            if row == i[0] and col == i[1]:
                break
            # newR = row + dr[d]
            # newC = col + dc[d]
            if row == i[0]:
                d = (d + 1) % 4
                cnt += 1
                while col != i[1]:
                    row = row + dr[d]
                    col = col + dc[d]


            if col == i[1]:
                d = (d + 1) % 4
                cnt += 1
                while row != i[1]:
                    row = row + dr[d]
                    col = col + dc[d]


        # newR = row + dr[d]
        # newC = col + dc[d]
        # if newR<0 or newR>=N or newC<0 or newC>=0:
        #     d = (d+1)%4
        #     cnt += 1
    print(cnt)