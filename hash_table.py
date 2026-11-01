class HashTable:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.threshold = 0.75

    def _hash(self, key: str) -> int:
        h = 0
        p = 31
        m = 10 ** 9 + 7
        for char in key:
            h = (h * p + ord(char)) % m
        return h % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                idx = self._hash(key)
                self.buckets[idx].append([key, value])

    def put(self, key: str, value: int):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return
        bucket.append([key, value])
        self.size += 1
        if self.size / self.capacity > self.threshold:
            self._resize()

    def get(self, key: str) -> str:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for item in bucket:
            if item[0] == key:
                return str(item[1])
        return "Error"

    def delete(self, key: str) -> str:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                val = bucket[i][1]
                bucket.pop(i)
                self.size -= 1
                return str(val)
        return "Error"

    def get_size(self) -> str:
        return str(self.size)


q = int(input().strip())
table = HashTable()
for _ in range(q):
    line = input().strip()
    parts = line.split()
    command = parts[0]

    if command == "put":
        key = parts[1]
        value = int(parts[2])
        table.put(key, value)

    elif command == "get":
        key = parts[1]
        print(table.get(key))

    elif command == "del":
        key = parts[1]
        print(table.delete(key))

    elif command == "size":
        print(table.get_size())
