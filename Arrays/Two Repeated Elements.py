for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    li = [0]*(n+3)
    count = 0
    ans = []
    for i in range(len(lis)):
        li[lis[i]]+=1
        if count ==2:
            break
        if lis[i]<n+1 and li[lis[i]]==2:
            ans.append(lis[i])
            count+=1
    print(*ans)
