class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        highest = 0
        j = 0
        i = 0
        n = len(nums)

        while i < n:

            if nums[i] == 1 and i!=n-1:
                j+=1
                i+=1
            
            elif nums[i] == 0:
                i+=1
                highest = max(highest , j)
                j = 0
            
            elif i == n-1 and nums[i] == 1:
                i+=1
                j+=1 
                highest = max(highest,j)
        
        return highest
