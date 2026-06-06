def check(nums,val):
    for i in range(len(nums)):
        if nums[i] == val:
            print(nums[i])
    

check([1,2,2,3,4,2],2)