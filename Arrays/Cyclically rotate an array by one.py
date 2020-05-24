lis_ans = []
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    ans = []
    ans.append(lis[n-1])
    for i in range(n-1):
        ans.append(lis[i])
    lis_ans.append(ans)


for i in lis_ans:
    print(*i)
