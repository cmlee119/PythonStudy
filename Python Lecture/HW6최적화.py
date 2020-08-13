import time
import bisect

class Set:
    #리스트 데이터가 정렬된 상태여야만 가능한 최적화
    def __init__(self, listInput = []):
        if type(listInput) == Set:
            self.data = listInput.data[:]
        elif type(listInput) == list:
            # 소팅을 한 후 중복 검사를 하는 방법
            # 함수 전체 시간복잡도 n log(n)
            self.data = []
            listSorted = sorted(listInput)  # n log(n)
            prevItem = None
            for item in listSorted: # n
                if item != prevItem:
                    self.data.append(item)
                prevItem = item

            # 소팅 없이 중복 검사를 하고 add 하는 방법 
            # 함수 전체 시간복잡도 n ^ 2
            # self.data = []
            # for item in listInput:
            #     self.add(item)
        else:
            print("__init__ error!!")
            self.data = []
        
    def add(self, elem):
        #시간 복잡도 n + n
        # if elem in self:
        #     return False
        # self.data.append(elem)
        # return True

        #시간 복잡도 n + log n
        index = bisect.bisect_left(self.data, elem)
        if self.data[index] == elem:
            return False
        
        self.data.insert(index, elem)
        return True
    
    def discard(self, elem):
        #시간 복잡도 n + n
        # if elem not in self:
        #     return False
        # self.data.remove(elem)
        # return True

        #시간 복잡도 n + log n
        index = bisect.bisect_left(self.data, elem)
        if self.data[index] != elem:
            return False

        self.data = self.data[:index] + self.data[index + 1:]
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
        # 함수 전체 시간 복잡도 n * m
        # for item in self:
        #     if item not in elem:
        #         return False
        # return True

        # 함수 전체 시간 복잡도 n + m
        left = self.data
        right = elem.data

        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):    # min(n, m)
            if left[leftIndex] == right[rightIndex]:
                leftIndex += 1
                rightIndex += 1
            elif left[leftIndex] > right[rightIndex]:
                rightIndex += 1
            else: # left[leftIndex] < right[rightIndex]:
                return False

        if leftIndex < len(left):
            return False

        return True
    
    def __ge__(self, elem):
        return elem <= self
    
    def __or__(self, elem):
        # 함수 시간 복잡도 n * m
        # newSet = Set(self)
        # for item in elem:
        #     newSet.add(item)
        # return newSet

        # 함수 시간 복잡도 n + m
        newSet = Set()

        left = self.data
        right = elem.data

        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):    # min(n, m)
            if left[leftIndex] == right[rightIndex]:
                newSet.data.append(left[leftIndex])
                leftIndex += 1
                rightIndex += 1
            elif left[leftIndex] > right[rightIndex]:
                newSet.data.append(right[rightIndex])
                rightIndex += 1
            else: # left[leftIndex] < right[rightIndex]:
                newSet.data.append(left[leftIndex])
                leftIndex += 1
                
        
        for index in range(leftIndex, len(left)):
            newSet.data.append(left[index])

        for index in range(rightIndex, len(right)):
            newSet.data.append(right[index])

        return newSet
    
    def __and__(self, elem):
        # 함수 시간 복잡도 n * m
        # newSet = Set()
        # for item in self:
        #     if item in elem:
        #         newSet.data.append(item) #add 쓰면 필요 없는 조건검사 하게됨
        # return newSet

        # 함수 시간 복잡도 n + m
        newSet = Set()

        left = self.data
        right = elem.data

        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):    # min(n, m)
            if left[leftIndex] == right[rightIndex]:
                newSet.data.append(left[leftIndex])
                leftIndex += 1
                rightIndex += 1
            elif left[leftIndex] > right[rightIndex]:
                rightIndex += 1
            else: # left[leftIndex] < right[rightIndex]:
                leftIndex += 1

        return newSet
    
    def __sub__(self, elem):
        # 함수 시간 복잡도 n * m
        # newSet = Set(self)
        # for item in elem:
        #     newSet.discard(item)
        # return newSet

        # 함수 시간 복잡도 n + m
        newSet = Set()

        left = self.data
        right = elem.data

        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):    # min(n, m)
            if left[leftIndex] == right[rightIndex]:
                leftIndex += 1
                rightIndex += 1
            elif left[leftIndex] > right[rightIndex]:
                rightIndex += 1
            else: # left[leftIndex] < right[rightIndex]:
                newSet.data.append(left[leftIndex])
                leftIndex += 1     
        
        for index in range(leftIndex, len(left)):
            newSet.data.append(left[index])

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

start = time.time()
c1 = Set([i for i in range(10)])
print(time.time() - start)

start = time.time()
c2 = Set([i for i in range(100)])
print(time.time() - start)

start = time.time()
c3 = Set([i for i in range(1000)])
print(time.time() - start)

start = time.time()
c4 = Set([i for i in range(10000)])
print(time.time() - start)

start = time.time()
c5 = Set([i for i in range(100000)])
print(time.time() - start)

# c1 = Set([i for i in range(10000)])
# c2 = Set([i for i in range(10000)])

# start = time.time()
# print(c1 <= c2)
# print(time.time() - start)