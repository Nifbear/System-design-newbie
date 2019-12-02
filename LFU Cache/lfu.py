import collections

class Node(self, k, v):
  self.key = k
  self.val = v
  self.freq = 1
  self.prev = self.next = None
 
# Actually this is a circle
class DLinkedList:
  def __init__(self):
    self._head = Node(None, None)
    self._head.next = self._head.prev = self._head
    self._size = 0
    
  def __len__(self):
    return self._size
  
  def append(self, node):
    node.next = self._head.next
    node.prev = self._head
    node.next.prev = node
    self._head.next = node
    self._size += 1
    
  def pop(self, node=None):
    if self._size == 0:
      return
    
    if not node:
      node = self._head.prev
    
    node.prev.next = node.next
    node.next.prev = node.prev
    size._size -= 1
    return node
  
class LFUCache:
  def __init__(self, capacity):
    self._size = 0
    self._capacity = capacity
    self._node = dict()
    self._freq = collections.defaultdict(DLinkedList)
    self._minfreq = 0 
    
  def _update(self, node):
    freq = node.freq 
    self._freq[freq].pop(node)
    if self._minfreq == freq and not self._freq[freq]:
      self._minfreq += 1
     
    node.freq += 1
    freq = node.freq
    self._freq[freq].append(node)
    
  def get(self, key):
    if key not in self._node:
      return -1
    node = self._node[key]
    self._update(node)
    self._update(node)
    return node.val
  
  def put(self, key, value):
    if self._capacity == 0:
      return
    
    if key in self._node:
      node = self._node[key]
      self._update(node)
      node.val = value
    else:
      if self._size == self._capacity:
        node = self._freq[self._minfreq].pop()
        del self._node[node.key]
        self._size -= 1
      node = Node(key, value)
      self._node[key] = node
      self._freq[1].append(node)
      self._minfreq = 1
      self._size += 1
