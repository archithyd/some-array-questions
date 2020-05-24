lis_ans = []
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    n1 = set(map(int, input().split()))
    n2 = set(map(int, input().split()))
    n3 = set(map(int, input().split()))
    val = n1.intersection(n2)
    ans = val.intersection(n3)
    lis = []
    for i in ans:
        lis.append(i)
    lis.sort()
    if len(lis)>0:
        lis_ans.append(lis)
    else:
        lis_ans.append([-1])

for i in lis_ans:
    print(*i)