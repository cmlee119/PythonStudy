class Set:
    def __init__(self, listInput = []):
        if type(listInput) == Set:
            self.data = listInput.data[:]
        elif type(listInput) == list:
            self.data = []
            for item in listInput:
                self.add(item)
        else:
            print("__init__ error!!")
            self.data = []
        
    def add(self, elem):
        if elem in self:
            return False
        self.data.append(elem)
        return True
    
    def discard(self, elem):
        if elem not in self:
            return False
        self.data.remove(elem)
        return True
    
    def clear(self):
        self.data.clear()
        
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return '{%s}' % ', '.join([str(item) for item in self])
    
    def __contains__(self, elem):
        return elem in self.data
    
    def __le__(self, elem):
        for item in self:
            if item not in elem:
                return False
        return True
    
    def __ge__(self, elem):
        return elem <= self
    
    def __or__(self, elem):
        newSet = Set(self)
        for item in elem:
            newSet.add(item)
        return newSet
    
    def __and__(self, elem):
        newSet = Set()
        for item in self:
            if item in elem:
                newSet.data.append(item) #add 쓰면 필요 없는 조건검사 하게됨
        return newSet
    
    def __sub__(self, elem):
        newSet = Set(self)
        for item in elem:
            newSet.discard(item)
        return newSet
    
    def __ior__(self, elem):
        self.data = (self | elem).data
        return self
        
    def __iand__(self, elem):
        self.data = (self & elem).data
        return self
        
    def __isub__(self, elem):
        self.data = (self - elem).data
        return self
    
    def __iter__(self):
        self.iterIndex = 0
        return self
    
    def __next__(self):
        if self.iterIndex >= len(self):
            raise StopIteration()
        result = self.data[self.iterIndex]
        self.iterIndex += 1
        return result


a = Set([1,2,3,4])
b = Set([2,3,4])

print(a)
print(b)
print()

a.discard(4)
b.discard(2)
print(a)
print(b)
print()

print(len(a))
print(1 in a)
print(1 in b)
print()

print(a | b)
print(a & b)
print(a - b)
print()

print(a <= b)
print(a <= a | b)
print(a >= b)
print(a >= a & b)
print()

b.clear()
print(b)