import json


try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []
def menu():
    print("1.add tasks")
    print("2.view tasks")
    print("3.update tasks")
    print("4.delete tasks")
    print("5.exit tasks")

while True:
    menu()
    
    choice=input("enter the chioce(1-5)")
    if choice=="1":
        task_name=input("enter task name: ")
        tasks.append(task_name)
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    elif choice=="2":
        for task in tasks:
            print(task)
    elif choice=="3":
        for i,task in enumerate(tasks,1):
            print(i,task)
        num=int(input("enter the number to update task"))
        new_task=input("enter the updated task: ")
        tasks[num-1]=new_task
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        
    elif choice=="4":
        for i,task in enumerate(tasks,1):
            print(i,task)
        num=int(input("enter the delete task number:"))
        tasks.pop(num-1)
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        
    else:
        print("exit tasks")
        break