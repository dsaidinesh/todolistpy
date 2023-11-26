todolist = []
while True:
    n = int(input("enter command:(1.add 2.remove 3.diplay "))
    if n==1:
        task = input("enter task: ")
        due = input("enter dude date: ")
        todolist.append({"description":task , "due" : due})
    elif n==2:
        num = int(input("enter number: "))
        if 0<num<len(todolist):
            todolist.pop(num)
    elif n==3:
        print(todolist)
    else:
        break



    
