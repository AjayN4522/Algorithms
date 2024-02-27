def binarySearch(arr,target):
    beg=0
    end=len(arr)-1
    if arr[beg]<arr[end]:
        while(beg<=end):
            mid=((beg+end)//2)
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                beg=mid+1
            else:
                end=mid-1
        return -1
    else:
        while(beg<=end):
            mid=((beg+end)//2)
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                end=mid-1
            else:
                beg=mid+1
if __name__ == '__main__':
    arr=[1,3,5,6,10,12,15,20,26,27]
    # arr=[27,26,20,25,12,10,6,5,3,1]
    target=1
    print(binarySearch(arr,target))
    