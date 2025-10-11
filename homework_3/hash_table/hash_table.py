class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        self.load_factor_threshold = 0.75

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self._resize()

        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
