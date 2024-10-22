class DLNode:
    def __init__(self, previous_node=None, data_portion=None, next_node=None):
        self.previous_node = previous_node
        self.data_portion = data_portion
        self.next_node = next_node

    def get_data(self):
        return self.data_portion

    def set_data(self, new_data):
        self.data_portion = new_data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

class LinkedDeque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def add_to_back(self, new_entry):
        new_node = DLNode(None, new_entry, None)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.set_previous_node(self.back)
            self.back.set_next_node(new_node)
            self.back = new_node
        self.size += 1

    def add_to_front(self, new_entry):
        new_node = DLNode(None, new_entry, None)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.set_next_node(self.front)
            self.front.set_previous_node(new_node)
            self.front = new_node
        self.size += 1

    def get_back(self):
        if not self.is_empty():
            return self.back.get_data()
        return None

    def get_front(self):
        if not self.is_empty():
            return self.front.get_data()
        return None

    def remove_front(self):
        if not self.is_empty():
            data = self.front.get_data()
            self.front = self.front.get_next_node()
            if self.front is not None:
                self.front.set_previous_node(None)
            else:
                self.back = None
            self.size -= 1
            return data
        return None

    def remove_back(self):
        if not self.is_empty():
            data = self.back.get_data()
            self.back = self.back.get_previous_node()
            if self.back is not None:
                self.back.set_next_node(None)
            else:
                self.front = None
            self.size -= 1
            return data
        return None

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def display(self):
        current = self.front
        display_list = []
        while current is not None:
            display_list.append(current.get_data())
            current = current.get_next_node()
        print("Deque contents:", display_list)


        

