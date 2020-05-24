def binary(arr, val) :
    if len (arr) >= 1 :
        mid = len (arr) // 2
        if arr[mid] == val :
            return True
        elif val > arr[mid] :
            return binary (arr[mid + 1 :len (arr)], val)
        else :
            return binary (arr[0 :mid], val)
    else :
        return False


def finder(lis1, k1) :
    for i in range (len (lis1)) :
        for j in range (1, len (lis1)) :
            if binary (lis1, (k1 - lis1[i] - lis1[j])) is True and k1-lis1[i]-lis1[j] != lis1[i] and k1-lis1[i]-lis1[j] != lis1[j] and lis1[i]!=lis[j]:
                return 1

    return 0


if __name__ == "__main__" :
    for _ in range (int (input ( ))) :
        n, k = map (int, input ( ).split ( ))
        lis = sorted(list (map (int, input ( ).split ( ))))
        print (finder (lis, k))
