lis_ans = []
for _ in range(int(input())):
    n = int(input())
    ans = 1
    while n>1:
        ans*=n
        n-=1
    lis_ans.append(ans)


for i in lis_ans:
    print(i)