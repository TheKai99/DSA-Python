# n = 5873


# while n != 0:

#     rem = n % 10
#     print(rem)

#     n = n//10


# n = 5873

# count = 0

# while n!=0:

#     count += 1
#     n = n//10

# print(count)
    

# check palindrome


def palindrome(n):

    num = n
    result = 0

    while num > 0:

        rem = num%10

        result = (result*10) + rem

        num = num//10

    return n == result

palindrome(1234)
print(palindrome(122221))