def searchInsert(nums,target):
    left = 0
    right = len(nums)-1

    while(left <= right):

            mid = (left+right)//2

            if nums[mid] == target: return mid
            if nums[mid] < target: left = mid+1
            if nums[mid] > target: right = mid-1
        
    return left


print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))