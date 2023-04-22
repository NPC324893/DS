
class Node:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_id(self, i):
        self.__id = i


class MaxHeap:
    def __init__(self):
        self.__heapList = []
        self.__heapSize = 0

    def get_heapList(self):
        return self.__heapList

    def get_heapSize(self):
        return self.__heapSize

    def isEmpty(self):
        if self.__heapSize == 0: return True
        else: return False

    def Insert(self, id ,name):
        new = Node(id, name)
        self.__heapList.append(new)
        self.__heapSize +=1
        self.reHeapUp(self.get_heapSize()-1)

    def reHeapUp(self, index):
        # start from index -1 (last element in the list)
        if index == 0:
            return

        if self.__heapList[index].get_id() > self.__heapList[(index - 1) // 2].get_id(): # parent index
            # SWAPPING
            temp = self.__heapList[index]
            self.__heapList[index] = self.__heapList[(index - 1) // 2]
            self.__heapList[(index - 1) // 2] = temp

        return self.reHeapUp(index -1)

    def remove(self):
        if self.isEmpty():
            return None

        removed = self.__heapList.pop(0)
        self.__heapSize -=1

        self.reHeapDown(0)
        return removed

    def reHeapDown(self, index):
        if self.__heapSize == 0:
            # heap is empty
            return

        if index >= self.__heapSize-1:
            # end of list
            return

        if len(self.__heapList)-1 >= index * 2 + 1:

            if self.__heapList[index].get_id() < self.__heapList[index * 2 + 1].get_id():
                largest = index * 2 + 1
                if len(self.__heapList)-1 >= index * 2 + 2:
                    if self.__heapList[largest].get_id() < self.__heapList[index * 2 + 2].get_id():
                        largest = index * 2 + 2

                temp = self.__heapList[index]
                self.__heapList[index] = self.__heapList[largest]
                self.__heapList[largest] = temp
                return self.reHeapDown(largest)




