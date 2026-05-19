tasks=[]
while True:
  print("TO DO LIST")
  print("1.Add Task\n2.View Task\n3.Update Task\n4.Delete Task\n5.Exit")
  choice=int(input("Enter your choice:"))
  if choice==1:
    task=(input("Enter Task:"))
    tasks.append(task)
    print("Task Added Successfully")
  elif choice==2:
    if len(tasks)==0:
        print("no tasks")
    else:
        print(tasks)
  elif choice==3:
    old_task=input("Enter the task:")
    if old_task in tasks:
        tasks.remove(old_task)
        new_task=input("Enter the new task:")
        tasks.append(new_task)
        print("updated successfully")
    else:
        print("Task not found")
  elif choice==4:
    task=input("Enter the Task:")
    if task in tasks:
        tasks.remove(task)
        print("removed successfully")
    else:
        print("task not found")
  elif choice==5:
    print("Exit")
    break
  else:
    print("Invalid choice")

