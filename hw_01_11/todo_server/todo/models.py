import json


from ..utils.binary_search import binary_search_by_id, binary_search


class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self.priority = priority
        self.location = None
        self.tag = None
        self.children = []
        Task.objects.append(self)

    def __eq__(self, other):
        return self.title == other.title and self.priority == other.priority

    def __hash__(self):
        return hash((self.title, self.priority))

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if int(value) in range(1, 11):
            self._priority = int(value)
        else:
            raise ValueError('Priority value is out of range')

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def get_list(cls):
        return cls.objects

    @classmethod
    def list_to_json(cls):
        task_list = [t.__dict__ for t in cls.objects]
        return json.dumps(task_list)

    def add_child(self, title, priority):
        child_task = Task(title, priority)
        self.children.append(child_task.id)

    def get_subtask(self):
        if not self.children:
            return []
        children = []
        for child_id in self.children:
            child_task = binary_search_by_id(Task.objects, child_id)
            if child_task is not None:
                children.append(child_task)
                children.extend(child_task.get_subtask())
        return children
