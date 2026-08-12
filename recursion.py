
def func(count=0):

    if count == 5:
        return

    print("hello")
    count+=1

    func(count)

    


func()
