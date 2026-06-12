def RemduplicateSortedArr(nums):

    unique = set()
    list = []

    for i in range(len(nums)):
        if nums[i] not in unique:
            unique.add(nums[i])
            list.insert(i,nums[i])
        else:
            list.insert(len(list)-1,nums[i])
        
    return  len(unique) , list

print(RemduplicateSortedArr([1,1,2,2,5])) # [1,2,5,_,_]



