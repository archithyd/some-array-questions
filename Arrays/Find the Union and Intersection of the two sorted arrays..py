lis_ans=[]
for _ in range(int(input())):
    m, n = map(int, input().split())
    lis1 = list(map(int, input().split()))
    lis2 = list(map(int, input().split()))
    dic = {}
    ans = []
    for i in lis1:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    for i in lis2:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    for i in dic.keys():
        ans.append(i)
    lis_ans.append(len(ans))

for i in lis_ans:
    print(i)