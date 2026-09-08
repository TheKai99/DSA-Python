class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        arranged = []

        positive = 0
        negative = 1

        for i in range(n):

            if nums[i] > 0:
                arranged.insert(positive,nums[i])
                positive+=2
            else:
                arranged.insert(negative,nums[i])
                negative+=2
        return arranged