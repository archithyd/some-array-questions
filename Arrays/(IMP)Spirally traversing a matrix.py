for _ in range(int(input())):
    li = []
    ans = []
    n,m = map(int, input().split())
    lis = list(map(int, input().split()))
    for i in range(n):
        li.append(lis[m*i:m*(i+1)])

    top = 0
    down = n-1
    right = m-1
    left = 0
    dir = 0
    while top<=down and left<=right:
        if dir == 0:
            for i in range(left,right+1):
                ans.append(li[top][i])
            top+=1
        elif dir == 1:
            for i in range(top,down+1):
                ans.append(li[i][right])
            right-=1
        elif dir == 2:
            for i in range(right,left-1,-1):
                ans.append(li[down][i])
            down-=1
        else:
            for i in range(down,top-1,-1):
                ans.append(li[i][left])
            left+=1

        dir = (dir+1)%4

    print(ans)
