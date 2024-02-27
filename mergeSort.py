def mergeSort(arr):
    if(len(arr)>1):
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        mergeSort(left_arr)
        # print(arr)
        mergeSort(right_arr)
        # print(arr)
        print(left_arr,right_arr)
        
        i=0
        j=0
        k=0
        while len(left_arr)>i and len(right_arr)>j:
            if left_arr[i]<right_arr[j]:
                print(left_arr[i],right_arr[j])
                arr[k]=left_arr[i]
                i+=1
                k+=1
            else:
                print(left_arr[i],right_arr[j])
                arr[k]=right_arr[j]
                j+=1
                k+=1
        while(i<len(left_arr)):
            arr[k]=left_arr[i]
            k+=1
            i+=1
        while(j<len(right_arr)):
            arr[k]=right_arr[j]
            k+=1
            j+=1
    return arr
    
if __name__ == '__main__':
    arr=[24,13,26,1,2,27,38,15]
    print(mergeSort(arr))