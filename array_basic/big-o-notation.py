



def find_element(array,value):
    n = len(array)
    lo = 0
    hi = n-1

    while(lo <= hi):

        mid = int((lo+hi)/2)
        if array[mid] == value: return mid
        elif array[mid] < value: lo = mid +1
        elif array[mid] > value: hi = mid-1
    
    return -1

array = [3, 7, 12, 19, 25, 38, 45, 56, 70, 84]

print(find_element(array, 38))   # Output: 5
print(find_element(array, 40))   # Output: -1