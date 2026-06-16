

def PlusOne(digit):

    input_digit = ''

    for num in digit:
        input_digit += str(num)
    
    output_digit = int(input_digit) + 1

    output = []

    while output_digit > 0:

        output.insert(0,output_digit % 10)

        output_digit = output_digit // 10

    return output





print(PlusOne([4,3,3,1]))

# digit = [1,2,3]

# result = ''

# for num in digit:

#     result += str(num)

# print(result)


# output = int(result) + 1
# print(output)

# check = str(output).split(',')
# print(check)