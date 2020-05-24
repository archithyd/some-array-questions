for _ in range(int(input())):
    n,m = map(int, input().split())
    lis = []
    for i in range(m):
        li = list(map(int, input().split()))
        for j in li:
            lis.append(j)
            if len(lis) == n*m:
                break

    print(sorted(lis)[len(lis)//2])