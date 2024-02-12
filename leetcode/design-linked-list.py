class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    # def as_list(self):
    #     curr = self.head
    #     arr = []
    #     while curr:
    #         arr.append(curr.val)
    #         curr = curr.next
    #     print(arr)
    def __init__(self):
        self.head = None
        self.size = 0 

    def get(self, index: int) -> int:
        # self.as_list()
        if index >= self.size:
            return -1
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        # self.as_list()
        temp = Node(val)
        temp.next = self.head
        self.head = temp  
        self.size += 1      

    def addAtTail(self, val: int) -> None:
        # self.as_list()
        temp = Node(val)
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = temp
        self.head = dummy.next
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        # self.as_list()
        if index > self.size:
            return
        temp = Node(val)
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        while index > 0:
            curr = curr.next
            index -= 1
        
        temp.next = curr.next
        curr.next = temp
        self.head = dummy.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # self.as_list()
        if index >= self.size:
            return
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
        while index > 0:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        self.head = dummy.next
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)