class Node:
    def __init__(self, key, val):
        self.key, self.value = key, val
        self.prev = self.next = None

        
class LRUCache:
    def remove(self, node: Node):
        prev_neighbour = node.prev
        next_neighbour = node.next
    
        prev_neighbour.next = next_neighbour
        next_neighbour.prev = prev_neighbour

    def add(self, node: Node):
        node.next = self.MRU.next
        node.prev = self.MRU
        
        self.MRU.next.prev = node
        self.MRU.next = node

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity
        self.MRU, self.LRU = Node(0,0), Node(0,0)
        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU
    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.add(self.hashMap[key])
            return self.hashMap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashMap:
            self.hashMap[key].value = value
            self.remove(self.hashMap[key])
            self.add(self.hashMap[key])
        else:
            new_node = Node(key, value)
            self.hashMap[key] = new_node
            self.add(new_node)

            if len(self.hashMap) > self.cap:
                oldest = self.LRU.prev
                del self.hashMap[oldest.key]
                self.remove(self.LRU.prev)
                

                
                
