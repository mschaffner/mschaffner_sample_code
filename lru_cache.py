'''
Problem source: https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
    exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently
    used item before inserting a new item.

'''
class Node:
    child = None
    parent = None
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        c = self.child.key if self.child else "None"
        p = self.parent.key if self.parent else "None"
        return "Node:{}, value:{}, child:{}, parent:{}".format(self.key, self.value, c, p)


class LRUCache(object):
    """
    Python LRU cache implementation using a hashmap to doubly linked list.
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = {}
        self.limit = capacity
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.child is not None:
            node.child.parent = node.parent
        else:
            self.tail = node.parent

        if node.parent is not None:
            node.parent.child = node.child
        else:
            self.head = node.child

    def set_head(self, node):
        node.child = self.head
        node.parent = None

        if node.child is not None:
            node.child.parent = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.data:
            node = self.data[key]
            self.remove(node)
            self.set_head(node)
            return node.value
        return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.data:
            current = self.data[key]
            current.value = value
            self.remove(current)
            self.set_head(current)
        else:
            new = Node(key, value)
            if len(self.data) >= self.limit:
                del self.data[self.tail.key]
                self.remove(self.tail)
                self.set_head(new)
            else:
                self.set_head(new)

            self.data[key] = new

