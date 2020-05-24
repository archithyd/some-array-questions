def finder(lis):
    for i in range(len(lis)):
        for j in range(i+1,len(lis)+1):
            print(lis[i:j])
            if sum(lis[i:j]) == 0:
                return "Yes"
    return "No"




if __name__ == "__main__":
    lis_ans = []
    for _ in range(int(input())):
        n = int (input ( ))
        lis = list (map (int, input ( ).split()))
        lis_ans.append(finder(lis))

    for i in lis_ans:
        pass
        # print(i)