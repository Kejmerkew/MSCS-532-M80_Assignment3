import time
import random
import string

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size  # number of slots
        self.table = [[] for _ in range(size)]  # initialize chains (lists)

    def _hash(self, key):
        """Hash function that maps a key to a table index."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # check if key already exists, update if so
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        """Search for a key and return its value if found."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Delete a key-value pair if it exists."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False


# ===== Experiment Code =====
def random_string(length=8):
    """Generate a random string key."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def measure_operations(n, table_size):
    """Measure insert, search, and delete performance for n elements."""
    ht = HashTableChaining(size=table_size)

    keys = [random_string() for _ in range(n)]

    # Measure inserts
    start = time.perf_counter()
    for key in keys:
        ht.insert(key, random.randint(1, 1000))
    insert_time = time.perf_counter() - start

    # Measure searches
    start = time.perf_counter()
    for key in keys:
        ht.search(key)
    search_time = time.perf_counter() - start

    # Measure deletes
    start = time.perf_counter()
    for key in keys:
        ht.delete(key)
    delete_time = time.perf_counter() - start

    load_factor = n / table_size
    return (n, load_factor, insert_time, search_time, delete_time)


# Run experiments
sizes = [1000, 2000, 5000, 10000]
table_size = 2000  # fixed slot count for testing effect of load factor

print("=== Hash Table with Chaining Performance ===")
print("n\tLoadFactor\tInsert(s)\tSearch(s)\tDelete(s)")
for n in sizes:
    n, alpha, ti, ts, td = measure_operations(n, table_size)
    print(f"{n}\t{alpha:.2f}\t\t{ti:.6f}\t{ts:.6f}\t{td:.6f}")
