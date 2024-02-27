def linearArray(arr,target):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if arr[i][j]==target:
                return [i,j]
    return [-1,-1]
if __name__ == '__main__':
    arr=[[2,5,3,4],
         [5,7,3,4],
         [8,3,2]]
    target=9
    print(linearArray(arr,target))
    