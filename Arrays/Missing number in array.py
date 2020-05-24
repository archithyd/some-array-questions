lis_ans =[]
for _ in range(int(input())):
    n = int(input())
    lis = sum(list(map(int, input().split())))
    dummy = []
    for i in range(n):
        dummy.append(i+1)

    lis_ans.append(sum(dummy)-lis)



for i in lis_ans:
    print(i)