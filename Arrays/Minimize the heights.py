for _ in range(int(input())):
    k = int(input())
    n= int(input())
    lis = list(map(int, input().split()))
    val1 = min (lis)
    val2 = max (lis)
    mid = (val1+val2)/2
    if val2- val1 > k :
        for i in range(len(lis)):
            if lis[i]>mid:
                lis[i]-=k
            else:
                lis[i]+=k
    val11 = min(lis)
    val21 = max(lis)
    print(val21-val11)



