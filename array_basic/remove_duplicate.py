def RemduplicateSortedArr(nums):

    unique = []
    list = []

    for i in range(len(nums)):
        if nums[i] not in unique:
            unique.append(nums[i])
    
        else:
            list.append(nums[i])
    
    k = len(unique)
    nums[:] = unique+list
        
    return k , nums

print(RemduplicateSortedArr([1,1,2,2,5])) # [1,2,5,
print(RemduplicateSortedArr([0,0,1,1,1,2,2,3,3,4])) # [1,2,5,
print(RemduplicateSortedArr([1,1,2]))



