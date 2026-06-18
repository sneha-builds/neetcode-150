# LRU Cache

"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1)average time complexity.
"""

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            
            node = self.cache[key]
            node.value = value
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
        else:
            
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                
                lru_node.prev.next = self.tail
                self.tail.prev = lru_node.prev
                
                del self.cache[lru_node.key]
            

            new_node = Node(key, value)
            self.cache[key] = new_node
            

            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node