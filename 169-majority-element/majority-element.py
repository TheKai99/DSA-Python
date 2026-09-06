class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()

        n =len(nums)
        limit = n/2

        count = 0

        for i in range(n-1):
            j = i+1

            if nums[i] == nums[j] and j == n-1:
                count+=2

                if count > limit:
                    return nums[i]

            if nums[i] == nums[j]:
                count +=1
            
            elif nums[i] != nums[j]:
                count+=1 
                if count > limit:

                    return nums[i]

        return nums[0]
            

        