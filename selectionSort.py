def selectionSort(arr):
    # minimum element
    for i in range(0,len(arr)):
        min=arr[i]
        temp=0
        for j in range(i,len(arr)):
            if arr[j]<min:
                min=arr[j]
                temp=j
                print(arr)
        if(temp):
            arr[i],arr[temp]=arr[temp],arr[i]
        print(arr)
    return arr   

    # for i in range(len(arr)-1,-1,-1):
    #     max=arr[i]
    #     temp=-1
    #     for j in range(i,-1,-1):
    #         if arr[j]>max:
    #             max=arr[j]
    #             temp=j
    #     if(temp>-1):
    #         arr[i],arr[temp]=arr[temp],arr[i]
    #     print(arr)
    # return arr   
if __name__ == '__main__':
    arr=[10,5,26,3,15,22]
    print(selectionSort(arr))
    
    