# Left Rotate the array by one place 

# arr = [1, 2 , 3 , 4 , 5]

# output

# arr = [2 , 3 , 4 , 5 , 1]


def Rotatearray(arr):

    n = len(arr)
    temp = arr[0]

    for i in range(1 , n):
        arr[i-1] = arr[i]

    arr[n-1] = temp
    return arr

print(Rotatearray([1,2,3,4,5]))
