def SecondLargesmall(nums):

    largest = nums[0]
    slargest = -1

    for i in range(1,len(nums)):

        if nums[i] > largest:
            slargest = largest
            largest = nums[i]
    

        elif nums[i] < largest and nums[i] > slargest:
            slargest = nums[i]

    return slargest

def SecondSmall(nums):

    smallest = nums[0]
    ssmallest = -1

    for i in range(1,len(nums)):

        if nums[i] < smallest:
            ssmallest = smallest
            smallest = nums[i]
        
        elif nums[i] > smallest and nums[i] < ssmallest:
            ssmallest = nums[i]

    return ssmallest


print(SecondLargesmall([1,2,4,7,7,5]))
print(SecondSmall([3,2,1,5,2]))