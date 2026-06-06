def isAnagram(s,t):

    if len(s) != len(t):
        return False
    
    char_freq = {}

    for char in s:
        char_freq[char] = char_freq.get(char,0) +1
    
    print(char_freq)
    

    for char in t:

        if char not in char_freq:
            return False
         
        char_freq[char] -= 1

        if char_freq[char] < 0:
            return False
    return True
 

        
        
        


    

print(isAnagram('cat','tac')) # True
print(isAnagram('anagram','nagaram')) # True
print(isAnagram('aa','a')) # False
print(isAnagram('cat','rat')) # False


# s = "string"

# s_list = list(s)
# print(s_list)