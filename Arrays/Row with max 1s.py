for _ in range(int(input())):
    n = list(map(int, input().split()))
    lis = list(map(int,input().rstrip("\n").split()))
    ans = 0
    val_sum = 0
    count = 0
    while count<n[0]:
        print(lis[n[1]*count:n[1]*(count+1)])
        val = sum(lis[n[1]*count:n[1]*(count+1)])
        if val>=val_sum:
            val_sum=val
            ans = count
        count+=1
    print(ans)


