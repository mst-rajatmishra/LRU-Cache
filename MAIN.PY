class Node:
    """Doubly Linked List Node."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to Node
        # Create dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value of the key if exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove from current position
            self._add_to_head(node)  # Add to head (most recently used)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Update the value of the key if it exists, otherwise add the key-value pair."""
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove LRU from the tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

# Test the LRUCache implementation
def test_lru_cache():
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1))  # cache is {1=1}
    print(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
    print(lRUCache.get(1))     # return 1
    print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))     # returns -1 (not found)
    print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))     # return -1 (not found)
    print(lRUCache.get(3))     # return 3
    print(lRUCache.get(4))     # return 4

# Run the test
test_lru_cache()

