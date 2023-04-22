class Node:

    def __init__(self, Data, left, right):  # initialize node’s fields
        self.Data = Data  # reference to Course’s name
        self.left = None  # reference to left node
        self.right = None  # reference to right node

    def getData(self):
        return self.Data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, i):
        self.Data = i

    def setLeft(self, n):
        self.left = n

    def setRight(self, n):
        self.right = n

    # •	toString method that returns a string containing the (student Data, GPA)
    def __str__(self):
        # return "(",self.getData())"
        return format(self.Data)


class BSTree:

    def __init__(self):
        self.Root = None

    def exist(self, data):
        return self.existNode(self.Root, data)

    def existNode(self, r, data):
        if r == None:
            return False
        if r.getData() == data:
            return True
        elif data < r.getData():
            return self.existNode(r.getLeft(), data)
        else:
            return self.existNode(r.getRight(), data)

    def insert(self, data):
        if self.exist(data):
            return False
        newest = Node(data, None, None)
        if self.Root == None:
            self.Root = newest  # special case: previously empty
        else:
            self.insertNode(self.Root, newest)
        return True

    def insertNode(self, r, temp):
        if temp.getData() < r.getData():
            if r.getLeft() == None:
                r.setLeft(temp)
                return
            self.insertNode(r.getLeft(), temp)
        else:
            if r.getRight() == None:
                r.setRight(temp)
                return
            self.insertNode(r.getRight(), temp)

    def remove(self, key):
        # 1. check if node exists
        if self.exist(key) == False:
            return False
        prev = None
        curr = self.Root
        # 2. find the node
        while True:
            if curr.getData() > key:
                prev = curr
                curr = curr.getLeft()
            elif curr.getData() < key:
                prev = curr
                curr = curr.getRight()
            else:
                break

        # 3. check if there exists a successor to the node
        if curr.getRight() is None:
            # 4. check if the node is the root
            if curr is self.Root:
                self.Root = self.Root.left
                return True

            # node is internal to the tree
            if prev.getLeft() is curr:
                prev.setLeft(curr.getLeft())
            else:
                prev.setRight(curr.getLeft())

            curr.setLeft(None)
            return True

        # Node does not have a left child
        if curr.getLeft() is None:
            # 4. check if the node is the root
            if curr is self.Root:
                self.Root = self.Root.right
                return True

            # node is internal to the tree
            if prev.getLeft() is curr:
                prev.setLeft(curr.getRight())
            else:
                prev.setRight(curr.getRight())

            curr.setRight(None)
            return True

        # 5. find inorder successor
        prev_succ, succ = curr, curr.right
        while succ.getLeft():
            prev_succ = succ
            succ = succ.getLeft()

        # 6. swap the values
        curr.setData(succ.getData())

        # 7. handle the right child of the successor
        if prev_succ is curr:
            prev_succ.setRight(succ.getRight())
        else:
            prev_succ.setLeft(succ.getRight())

        succ.setRight(None)

        return True
