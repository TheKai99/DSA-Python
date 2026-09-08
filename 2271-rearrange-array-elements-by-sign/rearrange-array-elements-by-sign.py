class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        arranged = [0]*n

        positive = 0
        negative = 1

        for i in range(n):

            if nums[i] > 0:
                arranged[positive] =nums[i]
                positive+=2
            else:
                arranged[negative] = nums[i]
                negative+=2
        return arranged