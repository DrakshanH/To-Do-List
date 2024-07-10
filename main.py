tasks = []
in_progress = []
done = []

def addTask():
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list!")


def deleteTask():
    listTasks()
    try:
        x = input("\nWhere do you want to delete the task from?\na) To-do\bb)In-Progress\bc)Done\n")
        if(x=='a'):
            task = int(input("Choose the task number to be deleted: "))
            if(task>=0 and task<len(tasks)):
                tasks.pop(task)
                print("Deleted succefully!")

            else:
                print(f"Task #{task} cannot be found!")

        elif(x=='b'):
            task = int(input("Choose the task number to be deleted: "))
            if(task>=0 and task<len(in_progress)):
                in_progress.pop(task)
                print("Deleted succefully!")

            else:
                print(f"Task #{task} cannot be found!")

        elif(x=='c'):
            task = int(input("Choose the task number to be deleted: "))
            if(task>=0 and task<len(done)):
                done.pop(task)
                print("Deleted succefully!")

            else:
                print(f"Task #{task} cannot be found!")

        else:
            print("Wrong input!")

    except:
        print("Invalid input</3")


def listTasks():
    if (not tasks) and (not done) and (not in_progress):
        print("\nNo tasks yet")
    else:
        if tasks:
            print("\nTo Do:-")
            for i, task in enumerate(tasks):
                print(f"Task #{i}. {task}")
        else:
            print("\nNo tasks in To-do")

        if in_progress:
            print("\nIn-Progress:-")
            for i, task in enumerate(in_progress):
                print(f"Task #{i}. {task}")

        else:
            print("\nNo tasks in In-Progress")

        if done:
            print("\nDone:-")
            for i, task in enumerate(tasks):
                print(f"Task #{i}. {task}")

        else:
            print("\nNo tasks in Done")


def shiftTasks():
    listTasks()
    if (not tasks) and (not done) and (not in_progress):
        print("\nNo tasks yet")
    else:
        a = input("\nWhere do you want to shift tasks from?\na) To-do\bb) In-Progress\bc) Done\n")
        if(a=='a'):
            if tasks:
                task = int(input("Choose the task number to be shifted: "))
                if(task>=0 and task<len(tasks)):
                    shift = tasks[task]
                    tasks.pop(task)                    
            else:
                print(f"Task #{task} cannot be found!")

        elif(a=='b'):
            if in_progress:
                task = int(input("Choose the task number to be shifted: "))
                if(task>=0 and task<len(in_progress)):
                    shift = in_progress[task]
                    in_progress.pop(task)                     
            else:
                print(f"Task #{task} cannot be found!")

        elif(a=='c'):
            if done:
                task = int(input("Choose the task number to be shifted: "))
                if(task>=0 and task<len(done)):
                    shift = done[task]
                    done.pop(task)                    
            else:
                print(f"Task #{task} cannot be found!")
        

        b = input("\nWhere do you want to shift tasks to?\na) To-do\bb) In-Progress\bc) Done\n")
        if(b=='a'):
            tasks.append(shift)
            print("Shifted succefully!")

        elif(b=='b'):
            in_progress.append(shift)
            print("Shifted succefully!")

        elif(b=='c'):
            done.append(shift)
            print("Shifted succefully!")




if __name__ == "__main__":
    # create a loop to run the app
    while True:
        print("\nPlease select one of the following options")
        print("---------------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Shift tasks")
        print("4. List tasks")
        print("5. Exit")

        ch = int(input("\nYour choice? "))
        if(ch == 1):
            addTask()

        elif(ch == 2):
            deleteTask()

        elif(ch == 3):
            shiftTasks()

        elif(ch == 4):
            listTasks()

        elif(ch == 5):
            break

        else: 
            print("\nInvalid choice, try again!")

    print("\n\nThank You for using the app!! wave wave")
