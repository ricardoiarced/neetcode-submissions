class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.m = 769
        self.buckets = [None] * self.m

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        i = key % self.m
        node = Node(key)
        node.next = self.buckets[i]
        self.buckets[i] = node

    def remove(self, key: int) -> None:
        i = key % self.m
        prev, cur = None, self.buckets[i]
        while cur and cur.val != key:
            prev, cur = cur, cur.next

        if cur is None:
            return
        elif prev is None:
            self.buckets[i] = cur.next
        else:
            prev.next = cur.next

    def contains(self, key: int) -> bool:
        i = key % self.m
        cur = self.buckets[i]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)