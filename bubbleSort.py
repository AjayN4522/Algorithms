def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr
if __name__ == '__main__':
    arr=[22,10,14,13,6,17]
    print(bubbleSort(arr))