class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if d < self.value:
            if self.left == None:
                self.left = Node(d)
                return True
            else:
                return self.left.insert(d)
        elif d > self.value:
            if self.right == None:
                self.right = Node(d)
                return True
            else:
                return self.right.insert(d)
        elif d == self.value:
            return False

    def find(self,d):
        if d == self.value:
            return True

        if d < self.value:
            if self.left == None:
                return False
            else:
                return self.left.find(d)
        elif d > self.value:
            if self.right == None:
                return False
            else:
                return self.right.find(d)

    def preOrderPrint(self):
        print(self.value)
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()

    def postOrderPrint(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.value)

    def minimumKey(curr):
        while curr.left:
            curr = curr.left

        return curr

    def delete(self,key):

        parent = None

        cur = self

        while cur and cur.value != key:

            parent = cur

            if key < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        if cur == None:
            return self

        if cur.left == None and cur.right == None:

            if cur != self:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None

            else:
                self = None

        elif cur.left and cur.right:

            successor = cur.right.minimumKey()

            val = successor.value

            self.delete(successor.value)

            cur.value = val

        else:

            if cur.left:
                child = cur.left
            else:
                child = cur.right

            if cur != self:
                if cur == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            else:
                self = child

        return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root == None:
            self.root = Node(d)
        else:
            return self.root.insert(d)

    def find(self,d):
        if self.root.value == None:
            return False
        else:
            return self.root.find(d)

    def preOrderPrint(self):
        if self.root == None:
            return False
        else:
            self.root.preOrderPrint()

    def postOrderPrint(self):
        if self.root == None:
            return False
        else:
            self.root.postOrderPrint()

    def delete(self,d):
        if self.root == None:
            return False
        else:
            # return self.root.delete(d)
            return self.root.delete(d)


t = Tree()
t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
t.preOrderPrint()
print()
t.delete(20)
t.postOrderPrint()
print()
print(t.find(1))
print(t.find(35))


