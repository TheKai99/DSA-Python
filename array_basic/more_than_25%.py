def findSpecialInteger(arr):

        hashmap = {}

        for num in arr:

            hashmap[num] = hashmap.get(num , 0) + 1
        

        for key in hashmap:

            if hashmap[key] > len(arr)//4:
                return key

print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))