class TodoList:
    def __init__(self, task_list):
        self.todo_list = task_list
        self.count = len(task_list)

    @property
    def undone_list(self):
        return list(filter(lambda item: not item['done'], self.todo_list))

    @property
    def done_list(self):
        return list(filter(lambda item: item['done'], self.todo_list))


# 默认表单
todo_list = [
    {"id": 1, "title": "出门买菜", "done": True},
    {"id": 2, "title": "回家做饭", "done": True},
    {"id": 3, "title": "运动30分钟", "done": True},
    {"id": 4, "title": "拉伸5分钟", "done": True},
    {"id": 5, "title": "学习一小时", "done": True},
    {"id": 6, "title": "休息20分钟", "done": True},
]


todo = TodoList(todo_list)
if __name__ == '__main__':
    print(todo.todo_list)
    print(todo.done_list)
    print(todo.undone_list)
