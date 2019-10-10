class Node:
  def __init__(self, k, v):
    self.key = k
    self.value = v
    self.next = None
    self.prev = None
    
class LRUCache:
  def __init__(self, capacity):
    self.d = {}
    self.capacity = capacity
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next, self.tail.prev = self.tail, self.head
  
  def put(self, key, value):
    if key in self.d:
      self._remove(self.d[key])
      
    node = Node(key, value)
    self.d[key] = node
    self._add(node)
    
    if len(self.d) > self.capacity:
      del self.d[self._remove(self.head.next)]
  
  def get(self, key):
    if key in self.d:
      n = self.d[key]
      self._remove(n)
      self._add(n)
      return node.value
    else:
      return -1
    
   
  def _remove(self, node) -> int:
    p, n = node.prev, node.next
    p.next = n
    n.prev = p
    return n.key
  
  def _add(self, node):
    p = self.tail.prev
    p.next = node
    node.prev = p
    node.next = self.tail
    self.tail.prev = node
