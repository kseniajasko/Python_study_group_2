class ListItem:

    data = None
    next = None

    def __init__(self, data):
        self.data = data

class LinkedList:

    head = None

    def __init__(self, data):
        self.head = ListItem(data=data)

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        tmp = self._current
        if tmp is not None:
            self._current = self._current.next
            return tmp
        else:
            raise StopIteration

    def add_element(self, data):
        new_element = ListItem(data=data)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = new_element

    def delete_element(self, data):
        if self.head == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return

        current = self.head
        while current is not None:
            if current.next.data == data:
                tmp = current.next
                current.next = current.next.next
                del tmp
                return
            else:
                current = current.next

    def print_list(self):
        if self.head is None:
            print('List has no element')
            return
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

    def extend(self, data_list):
        for element in data_list:
            self.add_element(element)

    def insert_at_start(self, data):
        new_element = ListItem(data)
        new_element.next = self.head
        self.head = new_element

    def insert_at_end(self, data):
        new_element = ListItem(data)
        if self.head is None:
            self.head = new_element
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_element

    def insert_at_index (self, index, data):
        if index == 0:
            self.insert_at_start(data)
        else:

            i = 0
            current = self.head
            while i < index - 1 and current is not None:
                current = current.next
                i = i + 1
            if current is None:
                raise IndexError('List Index Out Of Range')
            else:
                new_element = ListItem(data)
                new_element.next = current.next
                current.next = new_element

    def find_element(self, data):
        if self.head is None:
            print('List has no elements')
            return

        current = self.head
        while current is not None:
            if current.data == data:
               return current.data
            current = current.next
        return f'Item not found'

    @property
    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

# if __name__ == "__main__":
#     the_list = LinkedList(1)
#     the_list.add_element(2)
#     the_list.add_element(3)
#     the_list.add_element(10)
#     the_list.insert_at_start(11)
#     the_list.insert_at_end(20)
#     the_list.insert_at_index(2, 13)
#     the_list.extend([4,8,10])
#     the_list.print_list()
#
#     print(the_list.find_element(13))
#     print(the_list.length)
#
#     for element in the_list:
#         print(element.data)