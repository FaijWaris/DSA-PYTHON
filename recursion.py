count=0
def func():
    if count==4:
        return
    count+=1
    func()   
    print("faij")


func()
