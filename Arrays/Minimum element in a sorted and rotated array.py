def finder(arr,low,high):
    mid = (low+high)//2
    while low<high:
        if arr[mid]<arr[high]:
            return finder(arr,0,mid)
        else:
            return finder(arr,mid+1,high)

    return arr[low]


for _ in range(int(input())):
    n= int(input())
    lis = list(map(int,input().split()))
    print(finder(lis,0,n-1))



