def intersection(nums1, nums2):

        set1 = set()
        for num in nums1:
            if num not in set1:
                set1.add(num)

        print(set1)

        set2 = set()
        for num in nums2:
            if num not in set2:
                set2.add(num)

        print(set2)


        hashmap = {}

        for num in set1:
            hashmap[num] = hashmap.get(num , 0) +1

        for num in set2:
            hashmap[num] = hashmap.get(num , 0) + 1
        
        print(hashmap)


        result = []
        for key in hashmap:

            if hashmap[key] > 1:
                result.append(key)
        
        return result

print(intersection([4,9,5] , [9,4,9,8,4]))