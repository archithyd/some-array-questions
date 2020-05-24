def finder(lis):
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i] == lis[j]:
                return i+1

    return -1





if __name__ == "__main__":
    lis_ans = []
    for _ in range (int (input ( ))) :
        dic = {}
        val = -1
        n = int (input ( ))
        lis = list (map (int, input ( ).split ( )))
        lis_ans.append(finder(lis))
    for i in lis_ans:
        print(i)