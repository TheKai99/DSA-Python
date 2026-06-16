#   [0,0,1,1,1,2,2,3,3,4]   --  [0,1,2,3,4,0,1,1,2,3]


def RemoveDuplicate(nums):
    i = 0
    k = 0

    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
            k+=1
    return k , nums

print(RemoveDuplicate([0,0,1,1,1,2,2,3,3,4]))
        

