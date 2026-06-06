def two_sum(nums,target):

    output = []

    for i in range(len(nums)):
        for j in range(len(nums)):

            if i == j or j<=i:
                continue
            
            elif nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                return output



print(two_sum([3,4,5,6] , 7))
