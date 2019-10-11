class Node:

    def __init__(self, query, results):
        self.query = query
        self.results = results
        self.prev = None
        self.next = None
 

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
       
    def move_to_front(self, node): pass # ...
    def append_to_front(self, node): pass # ...
    def remove_from_tail(self): pass # ...
    

class Cache(object):
    
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {} # key: query, value: node
        self.linked_list = LinkedList()
    
    def get(self, query):    
        node = self.lookup.get(query)
        if node is None:
            return None
        self.linked_list.move_to_front(node)
        return node.results
    
    def set(self, results, query):
        node = self.lookup.get(query)
        if node is not None:
            node.results = results
            self.linked_list.move_to_front(node)
        else:
            if self.size == self.MAX_SIZE:
                self.lookup.pop(self.linked_list.tail.query, None)
                self.linked_list.remove_from_tail()
            else:
                self.size += 1
            new_node = Node(query, results)
            self.linked_list.append_to_front(new_node)
            self.lookup[query] = new_node
