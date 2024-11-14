inp = """
***********************

1. Aad Task
2. Show Tasks
3. Finished a Task ?
4. Delete Task

***********************

Choose : """

tasks=[]


class Task:
    def __init__(self,task,finished=False):
        self.task = task
        self.finished = finished
    def addTask(self,task):
        self.task = task
    def finishTask(self,finished):
        self.finished = finished

def choice():
    choice = int(input(inp))
    if choice not in [1,2,3,4]:
        choice = int(input(inp))
    return choice

def addTask():
    newTask = input("Your new task ? : ")
    tasks.append(Task(newTask))


def showTasks():
    print("\nMy tasks :")
    for task in tasks:
        print("- "+task.task,end=" ")
        if task.finished==True:
            print("Finished !")
        else:
            print("")



def deleteTask():
    if len(tasks)==0:
        print("Please aad tasks !")
    else:
        showTasks()
        num = int(input("Which task do you want to delete ? : "))
        tasks.remove(tasks[num-1])

def finishTask():
    if len(tasks)==0:
        print("Please aad tasks !")
    else:
        showTasks()
        num = int(input("Which task did you finish ? : "))
        tasks[num-1].finishTask(True)

while True:
    n=choice()
    if n==1:
        addTask()
    elif n==2:
        showTasks()
    elif n==3:
        finishTask()
    else:
        deleteTask()