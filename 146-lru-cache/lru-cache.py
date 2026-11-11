class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.nxt=None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache={}
        # key->Node
        self.capacity = capacity

        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)

        self.head.next=self.tail
        self.tail.prev=self.head
        # head<->lru<->.........<->mru<->tail

    def remove(self,node):
        pnode=node.prev
        nnode=node.next
        pnode.next=nnode
        nnode.prev=pnode
    
    def insert(self,node):
        # inserts at tail
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            oldnode = self.cache[key]
            self.remove(oldnode)
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        else:
            length = len(self.cache)
            if length < self.capacity:
                newnode = Node(key,value)
                self.cache[key] = newnode
                self.insert(newnode)
            else:
                nodetoberemove = self.head.next
                self.remove(nodetoberemove)
                del self.cache[nodetoberemove.key]
                node = Node(key, value)
                self.insert(node)
                self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)