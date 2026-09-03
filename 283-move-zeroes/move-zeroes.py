class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)

        for i in range(n-1):

            j = i+1

            while nums[i] == 0 and j < n:

                if nums[j] == 0:
                    j+=1
                
                else:
                    nums[j],nums[i] = nums[i],nums[j]