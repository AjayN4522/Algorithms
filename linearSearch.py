def linearSearch(arr,target,c):
    n=len(arr)
    # for i in range(0,n):
    #     if arr[i]==target:
    #         return i
    # return -1
    
    for i in c:
        if i==target:
            print("index is :",(c.index(i)))
            return True
    return -1
if __name__ == '__main__':
    arr=[2,4,5,6,3,1,7]
    c="AjayKumar"
    target="b"
    print(linearSearch(arr,target,c))
    

