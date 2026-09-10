class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 0
        n = len(nums)
        last_smaller = float('-inf')
        nums.sort()

        temp = 0

        for i in range(n):

            if nums[i] == last_smaller:
                pass

            elif nums[i]-1 == last_smaller:

                temp +=1
                last_smaller = nums[i]
            
            elif nums[i]-1 != last_smaller:
                temp = 1
                last_smaller = nums[i]

            count = max(temp,count)

        return count


        