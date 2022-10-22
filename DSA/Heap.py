import math
class Heap:
    def __init__(self, capacity):
        self.first = 0
        self.array = [0] * capacity
        self.capacity = capacity
        self.fillCount = 0

    def ParentIdx(self,childIdx):
        return (childIdx - 1)//2

    def LeftChildIdx(self,pIdx):
        return 2 * pIdx + 1

    def rightChildIdx(self,pIdx):
        return 2 * pIdx + 2

    def heightOfHeap(self):
        logBase2 = math.log2(self.size + 1)
        return math.ceil(logBase2)

    def isLeafNode(self,idx):
        if self.fillCount < 2 * idx:
            return True
        return False

    def insert(self, num):
        if self.fillCount == self.capacity:
            raise('array is full')
        self.array[self.fillCount] = num
        self.fillCount += 1
        self.heapifyUp()


    def heapifyUp(self):
        childIdx = self.fillCount-1
        childVal = self.array[childIdx]
        parentIdx = self.ParentIdx(childIdx)
        parentVal = self.array[parentIdx]
        if childVal < parentVal:
            self.swap(childIdx,parentIdx)



    def swap(self,childIdx,parentIdx):
        self.array[childIdx],self.array[parentIdx] = self.array[parentIdx],self.array[childIdx]



hp = Heap(7)

hp.insert(7)
hp.insert(6)
hp.insert(5)
hp.insert(3)
hp.insert(11)
hp.insert(33)

print(hp.array)

parentidx = hp.ParentIdx(5)
print(parentidx)

