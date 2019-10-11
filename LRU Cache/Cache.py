class Node:

    def __init__(self, results):
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
        self.lookup = {} #
