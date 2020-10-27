class Node:
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self,d):
        self.data = d
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)
    # Endurkvæmt fall sem bætir aftast á listann.
    def append(self,d):
        data = Node(d)
        if self.next == None:
            self.next = data
            data.prev = self
        else:
            self.next.append(d)
    # Þinn kóði hér

    # Endurkvæmt fall sem prentar listann.
    def printList(self):
        print(self.data, end=" ")
        if self.next == None:
            return True
        else:
            self.next.printList()
    # Þinn kóði hér

    # Endurkvæmt fall sem athuga hvort stak d er í listanum.
    def find(self,d):
        if self.data == d:
            return True
        if self.next == None:
            return False
        else:
            return self.next.find(d)
    # Þinn kóði hér

    # Endurkvæmt fall sem eyðir staki d úr listanum.
    def delete(self,d):
        if self.next == None:
            return False
        elif self.data == d:
            self.prev.next = self.next
            self.next.prev = self.prev
            return True
        else:
            return self.next.delete(d)

# Þinn kóði hér

class DLL:
    # Smiður, núllstillir Haus listans
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.
    def push(self,d):
        data = Node(d)
        if self.head == None:
            self.head = data
        else:
            self.head.prev = data
            data.next = self.head
            self.head = data

    # Þinn kóði hér

    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.
    def append(self,d):
        data = Node(d)
        if self.head == None:
            self.head = data
        else:
            self.head.append(d)
    # Þinn kóði hér

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node.
    def printList(self):
        current = self.head
        if self.head != None:
            current.printList()
        print()
    # Þinn kóði hér

    # Finnur stak d í ef til -> kallar á endurkvæmnt fall í Node.
    def find(self,d):
        if self.head == None:
            return False
        elif self.head.data == d:
            return True
        else:
            output = self.head.find(d)
        return output
    # Þinn kóði hér

    # Eyðir staki d úr lista ef til -> kallar á endurkvæmnt fall í Node.
    def delete(self,d):
        if self.head == None:
            return False
        if self.head.data == d:
            self.head = self.head.next
            self.head.prev = None
            return True
        else:
            return self.head.delete(d)

# Þinn kóði hér

# Keyrslurútína
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7
dbl.push(1)             # 1 5 7
dbl.push(0)             # 0 1 5 7
dbl.append(10)          # 0 1 5 7 10
dbl.printList()
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList()
print()
print(dbl.find(5))      # False
print(dbl.find(7))      # True