import bisect

# Getted from http://stackoverflow.com/questions/1109804/does-python-have-a-sorted-list

class sortlist:
    def __init__(self, list):
        self.list = list
        self.sort()
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __setitem__(self, index, value):
        self.list[index] = value
    
    def sort(self):
        l = []
        for i in range(len(self.list)):
            bisect.insort(l, self.list[i])
        self.list = l
        self.len = len(self.list)
    def delete (self, index):
        del self.list[index]
        self.len -= 1
    def insert(self, value):
        bisect.insort(self.list, value)
        self.len += 1

    def show(self):
        print self.list

    def search(self,value):
        if not self.list: return
        left = bisect.bisect(self.list, value)
        return left-1

    def search_left(self,value):
        if not self.list: return
        left = bisect.bisect_left(self.list, value)
        return left-1
