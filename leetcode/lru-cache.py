class DoubleListNode:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None
class LRUCache:
    # def as_list(self):
    #     n = self.dummy.next
    #     arr = []
    #     # while n:
    #     #     arr.append(self.key_value_node[n.key])
    #     #     n = n.next
    #     print(arr)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value_node = {}
        self.dummy = DoubleListNode(-1)
        self.curr = self.dummy
        # self.as_list()

    def get(self, key: int) -> int:
        # self.as_list()
        if key not in self.key_value_node:
            return -1
        value = self.key_value_node[key][0]
        node = self.key_value_node[key][1]
        if node.next != None:
            # delete it from where it was
            node.prev.next = node.next
            node.next.prev = node.prev
            # insert it at the last
            self.curr.next = node
            node.prev = self.curr
            node.next = None
            self.curr = node
            self.key_value_node[key] = (value, self.curr)
        return value

    def put(self, key: int, value: int) -> None:
        # self.as_list()
        if key in self.key_value_node:
            node = self.key_value_node[key][1]
            if node.next != None:
                # delete that node from where it was
                node.prev.next = node.next
                node.next.prev = node.prev
                # insert it to the last  
                self.curr.next = node
                node.prev = self.curr
                node.next = None
                self.curr = node
            # update the hashmap
            self.key_value_node[key] = (value, node)
        else:
            if len(self.key_value_node) == self.capacity:
                deleted = self.dummy.next
                if deleted == self.curr:
                    self.curr = self.curr.prev
                self.dummy.next = deleted.next
                if deleted.next:
                    deleted.next.prev = self.dummy
                
                # delete from hashmap
                del self.key_value_node[deleted.key]
            temp = DoubleListNode(key)
            self.curr.next = temp
            temp.prev = self.curr
            self.curr = temp
            self.key_value_node[key] = (value, temp)
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
c = 5
1 : 2
2 : 2
3 : 4
4 : 5
6 : 2


'''