# LOW = "1"
# MEDIUM = "2"
# HIGH = "3"
# STATUS = {
#     LOW: "low",
#     MEDIUM: "medium",
#     HIGH: "high"
# }
# Главное меню
def main_menu():
    tasks = load_tasks()
    while True:
        print("1 - Создать новую задачу")
        print("2 - Просмотреть задачи")
        print("3 - Обновить задачу")
        print("4 - Удалить задачу")
        print("0 - Выйти из программы")
        user_choice = input("Ваш выбор: ")
        if user_choice == "1":
            new_task(tasks)
            save_tasks(tasks)
        elif user_choice == "2":
            view_tasks(tasks)
        elif user_choice == "3":
            print("Функции обновлении пока нету")
        elif user_choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif user_choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

# Создание новой задачи
def new_task(tasks):
    name = input("Название: ")
    description = input("Описание: ")
    priority = ""
    while priority not in {"1", "2", "3"}:
        priority = input("Приоритет 1 - low, 2 - medium, 3 - high: ")
    status = ""
    while status not in {"1", "2", "3"}:
        status = input("Статус 1 - новая, 2 - в процессе, 3 - завершена: ")
    task_id = str(max(map(int, tasks.keys()), default=0) + 1)
    tasks[task_id] = {
        "name": name,
        "description": description,
        "priority": {"1": "low", "2": "medium", "3": "завершена"}[priority],
        "status": {"1": "новая", "2": "в процессе", "3": "завершена"}[status],
    }
# сохраняем что понаписали
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            line = ",".join([task_id, task["name"], task["description"], task["priority"], task["status"]])
            file.write(line + "\n")

# Загружаем что понаписали
def load_tasks():
    tasks = {}
    with open("tasks.txt", "r") as file:
        for line in file:
            task_id, name, description, priority, status = line.strip().split(",")
            tasks[task_id] = {
                "name": name,
                "description": description,
                "priority": priority,
                "status": status,
            }
    return tasks

# выводим на экран
def view_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    print("Список задач:")
    for task_id, task in tasks.items():
        print(f"ID: {task_id} Название: {task['name']} Описание: {task['description']} Приоритет: {task['priority']} Статус: {task['status']}")
    while True:
        print("1 - Отобразить задачи в изначальном виде")
        print("2 - Отсортировать по статусу")
        print("3 - Отсортировать по приоритету")
        print("4 - Осуществить поиск по названию или описанию")
        print("0 - Выйти из меню")
        user_choice = input("Ваш выбор: ")
        if user_choice == "1":
            print("v processe")
        elif user_choice == "2":
            print("v processe")
        elif user_choice == "3":
            print("v processe")
        elif user_choice == "4":
            print("v processe")
        elif user_choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
        


# DELETE TASK

def delete_task(tasks):
    task_id = input("Введите ID задачи для удаления: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Задача {task_id} удалена.")
    else:
        print("Задача с таким ID не найдена.")



main_menu()