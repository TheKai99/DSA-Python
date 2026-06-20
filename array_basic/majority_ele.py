
def MajorityElement(nums):

    dict = {}
    length = len(nums)/2

    for num in nums:
        dict[num] = dict.get(num , 0) + 1

    for key in dict:
        if dict[key] > length:
            return key
        