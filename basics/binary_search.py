def locate_number(arr,query):
    lo,hi= 0, len(arr)-1
    
    
    while lo<=hi:
        mid=(lo+hi)//2             #mid should be inside of while loop for new value of mid for each iteration #bodmas imp
        mid_num=arr[mid]        
        print("--o--W--o--")
        if mid_num==query:
            return mid
        elif mid_num>query:
            hi=mid-1
        elif mid_num<query:
            lo=mid+1
    return -1


arr=[1,2,3,4,5,6,7]
# print(type(arr))
query=3
result=locate_number(arr,query)
print("the number is found at the index",result)