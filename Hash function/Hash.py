
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [ [] for i in range(self.MAX)]

# Hash function
    def get_hash (self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 310
    t['march 7'] = 420
    t['march 8'] = 300
    t['march 17'] = 490
    # del t['march 6']
    print(t.arr)