# [1,2,3,1]




def contain_duplicate(nums):

    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False






print(contain_duplicate([1,2,3,1]))
print(contain_duplicate([1,2,3,4]))
print(contain_duplicate([1,1,1,3,3,4,3,2,4,2]))



