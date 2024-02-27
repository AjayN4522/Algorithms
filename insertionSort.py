def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                print(arr)
            else:
                break
    return arr     
if __name__ == '__main__':
    arr=[5,8,2,4,3,9]
    print(insertionSort(arr))
    