tasks = []

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số không hợp lệ. Không thể hoàn thành công việc.")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa công việc: {removed['name']}")
    else:
        print("Chỉ số không hợp lệ. Không thể xóa công việc.")

def list_tasks():
    for i, task in enumerate(tasks):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i + 1}. {status} {task['name']}")

if __name__ == "_main_":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    complete_task(0)
    list_tasks()
    delete_task(1)
    list_tasks()