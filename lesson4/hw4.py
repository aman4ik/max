import datetime

todoList = []

while True:
    print()
    operation = int(input("Add todo (1)? or show todos (2)?"))
    print()

    if operation == 1:
        todo = input("введите задачу: ")
        date = datetime.datetime.now()
        todoList.append({
            'todo': todo,
               'date': date
         })
        print("Задача успешно добавлена!")
        print()
    elif operation == 2:
        for todo in todoList:
                print()
                print(f'Задача: {todo["todo"]}\nдата создания: {todo["date"]}')