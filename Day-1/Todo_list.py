import json
try:
    with open("todo_list.json", "r") as f:
            todo_list = json.load(f)
except FileNotFoundError:
    todo_list = []
while True:
    print("""1. Add task
2. show task
3. complete task
4. delete task
5. update task
6. quit
    """)
    try:
        user_input = int(input("Enter the respected number of the command: "))
    except ValueError as e:
        print(f"Error: {e}\nPlease enter a valid value only.")
        continue
    if user_input == 1:
      key = input("Enter you task name: ").strip()
      todo_list.append({"task": key,"done": False})
      with open("todo_list.json", "w") as f:
        json.dump(todo_list, f, indent=4)
    elif user_input == 3:
        for i, item in enumerate(todo_list, start=1):
            mark = "x" if item["done"] else " "
            print(f"{i}. [{mark}] {item['task']}")
        try:
            
            task_done_name = int(input("enter the task number you complete[for example enter 1 for task one and 2 for task two]: "))
        except ValueError as e:
            print(f"Error: {e}\nPlease enter a valid value only.")
            continue
        index = task_done_name - 1
        if index < 0 or index >= len(todo_list):
            print("Invalid task number")
            continue
        is_task_done = input(f"Is your task is done enter(T/F): ")
        if is_task_done == "T":
            todo_list[index]["done"] = True
            with open("todo_list.json", "w") as f:
                json.dump(todo_list, f, indent=4)
        else:
            todo_list[index]["done"] = False
            with open("todo_list.json","w") as f:
                json.dump(todo_list,f,indent=4)

    elif user_input == 4:
       for i, item in enumerate(todo_list, start=1):
            mark = "x" if item["done"] else " "
            print(f"{i}. [{mark}] {item['task']}")
       try:
        delete = int(input("which task do you wann delete[in number like 2 for task two]: "))
       except ValueError as e:
            print(f"Error: {e}\nPlease enter valid value only.")
            continue
       index_1 = delete - 1
       if index_1 < 0 or index_1 >= len(todo_list):
            print("Invalid task number")
            continue
       del todo_list[index_1]
       with open("todo_list.json", "w") as f:
        json.dump(todo_list, f, indent=4)
    elif user_input == 5:
        try:
            key_to_update = int(input("enter you task index to update index: "))
        except ValueError as e:
            print(f"Error: {e}\nPlease enter valid value only.")
            continue
        index_2 = key_to_update - 1
        if index_2 < 0 or index_2 >= len(todo_list):
            print("Invalid task number")
            continue
        new_value = input("assign it into new value: ")
        todo_list[index_2]["task"] = new_value
        with open("todo_list.json","w") as f:
            json.dump(todo_list,f,indent=4)
    elif user_input == 2:
        for i, item in enumerate(todo_list, start=1):
            mark = "x" if item["done"] else " "
            print(f"{i}. [{mark}] {item['task']}")
    elif user_input == 6:
       break
