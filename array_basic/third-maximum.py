def ThirdMaximum(nums):
     
    largest = nums[0]
    secondlargest = float('-inf')
    thirdlargest = float('-inf')

    for i in range(0,len(nums)):

        if nums[i]>largest:
            secondlargest = largest
            largest = nums[i]
        
        elif nums[i]<largest and nums[i] > secondlargest:
            secondlargest = nums[i]
    return secondlargest
    
    # for i in range(0,len(nums)):

    #     if len(nums) == 2:
    #         thirdlargest = largest
        
    #     if len(nums) == 1:
    #         thirdlargest = largest

    #     if nums[i] > secondlargest and nums[i] != largest:
    #         thirdlargest = secondlargest
    #         secondlargest = nums[i]
        
    #     elif nums[i] < secondlargest and nums[i] > thirdlargest:
    #         thirdlargest = nums[i]
    
    # return thirdlargest
        
        
print(ThirdMaximum([3,2,1]))
print(ThirdMaximum([1,2]))
print(ThirdMaximum([1]))
print(ThirdMaximum([1,1,2]))
    