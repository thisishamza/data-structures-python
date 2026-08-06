class HashMap:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    # O(1)
    def __len__(self):
        return self.size

    # O(1) - Average
    # O(n) - worst
    # depends on the quality of hash function
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return True
        return False

    # O(1) - Average
    # O(n) - worst
    # depends on the quality of hash function
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size  += 1

    # O(1) - Average
    # O(n) - worst
    # depends on the quality of hash function
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key not found")

    # O(1) - Average
    # O(n) - worst
    # depends on the quality of hash function
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    # O(n)
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n)
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n)
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - Linear in key length
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0
        for char in key_string:
            hash_result = (hash_result * 31 + ord(char)) % self.capacity
        return hash_result


if __name__ == "__main__":
    hash_map = HashMap(10)
    hash_map.put('name', 'hamza')
    hash_map.put('age', 129)
    hash_map.put('gender', 'male')
    print(hash_map.items())
    print(hash_map.keys())
    print(hash_map.values())
    print(hash_map.buckets)
    print(hash_map.get('age'))
    hash_map.remove('name')
    print(hash_map.items())
    hash_map.put('name', 'muhammad')
    print(hash_map.items())
    hash_map.put('name', 'hamza')
    print(hash_map.items())
