for _ in range(int(input())):
    n = int(input())
    lis = sorted(set(map(int, input().split())))
    val=0
    count=1
    for i in range(1,len(lis)):
        if lis[i]-lis[i-1] == 1 or lis[i]-lis[i-1] == 0:
            count+=1
        else:
            val = max(val,count)
            count = 1
    print(max(val,count))
