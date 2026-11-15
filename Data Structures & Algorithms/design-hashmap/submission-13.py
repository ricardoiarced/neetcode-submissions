class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.size = 10_000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        i = key % self.size
        node = self.buckets[i]

        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next
        
        new_node = Node(key, value)
        new_node.next = self.buckets[i]
        self.buckets[i] = new_node

    def get(self, key: int) -> int:
        i = key % self.size
        node = self.buckets[i]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.size
        prev, node = None, self.buckets[i]

        while node:
            if node.key == key:
                if prev is None:
                    self.buckets[i] = node.next
                else:
                    prev.next = node.next
                return
            prev, node = node, node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)