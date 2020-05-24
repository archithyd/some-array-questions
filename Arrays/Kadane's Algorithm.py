lis_ans = []
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    curr = lis[0]
    total = lis[0]
    for i in range(1,len(lis)):
        curr = max(lis[i],curr+lis[i])
        total = max(total,curr)
    lis_ans.append(total)

for i in lis_ans:
    print(i)
