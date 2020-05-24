#incomplete

def PrintDuplicates(arr, n):
    lis = []
    for i in range(len(arr)):
        arr[arr[i] % n] = arr[arr[i] % n] + n

    for i in range(n):
        if arr[i] >= n*2:
            lis.append(i)
    if len(lis)>0:
        print(lis)
    else:
        print(-1)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        PrintDuplicates(arr, n)
        print(" ")
