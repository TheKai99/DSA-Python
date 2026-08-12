s = "GaDbZzTJl"

q = ["G" , "D" , "d" , "l" , "b" , "t" , "J" , "l" , "L"]


hash_list = {}

for ch in s:
    ascii = ord(ch)
    index = ascii-57
    hash_list[index]  = hash_list.get(index , 0)+1

for ch in q:
    ascii = ord(ch)
    index = ascii-57
    print(f"{ch} = {hash_list.get(index ,0)}")
