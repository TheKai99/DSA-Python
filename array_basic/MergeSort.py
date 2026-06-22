# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]


# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

def merge(nums1 , m , nums2 , n):

    i = 0
    for num in nums2:
        nums1[m+i] = num
        i+=1
    
    nums1.sort()
    return nums1

    
print(merge([1,2,3 ,0 ,0 ,0] , 3 , [2,5,6] ,3 ))

