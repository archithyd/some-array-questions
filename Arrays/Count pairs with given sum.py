lis_ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    lis = list(map(int, input().split()))
    ans = 0
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i]+lis[j] == m:
                ans+=1

    lis_ans.append(ans)


for i in lis_ans:
    print(i)