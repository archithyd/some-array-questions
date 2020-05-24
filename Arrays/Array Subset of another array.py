for _ in range(int(input())):
    n, m = map(int, input().split())
    lis1 = list(map(int, input().split()))
    lis2 = list(map(int, input().split()))
    dic = {}
    for i in lis1:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    count = len(lis2)
    for i in lis2:
        if i in dic:
            count-=1

    if count == 0:
        print("Yes")
    else:
        print("No")