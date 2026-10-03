class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.m = 307
        self.buckets = [None] * self.m

    def put(self, key: int, value: int) -> None:
        i = key % self.m
        cur = self.buckets[i]
        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next
        
        node = Node(key, value)
        node.next = self.buckets[i]
        self.buckets[i] = node

    def get(self, key: int) -> int:
        cur = self.buckets[key % self.m]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.m
        prev, cur = None, self.buckets[i]
        while cur and cur.key != key:
            prev = cur
            cur = cur.next
        
        if cur is None:
            return
        if prev is None:
            self.buckets[i] = cur.next
        else:
            prev.next = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)