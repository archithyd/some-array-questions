for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    i = 0
    li1 = []
    stc1 = []
    stc2 = []
    ans = []
    while i<n:
        val = [lis.pop (0)]
        if val[0] == 1:
            val.append(lis.pop(0))
            if val[1] == 1:
                val.append(lis.pop(0))
            i+=1
        else:
            val.append(lis.pop(0))
            if val[1] == 1:
                val.append(lis.pop(0))
            i+=1
        li1.append(val)

    for i in li1:
        if i[0] == 1:
            if i[1] == 1:
                stc1.append(i[2])
            else:
                if len(stc1) == 0:
                    ans.append(-1)
                else:
                    ans.append(stc1.pop(len(stc1)-1))
        else:
            if i[1] == 1:
                stc2.append (i[2])
            else :
                if len (stc2) == 0 :
                    ans.append(-1)
                else :
                    ans.append(stc2.pop (len (stc2) - 1))

    print(*ans)
