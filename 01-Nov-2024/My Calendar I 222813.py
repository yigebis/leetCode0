# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class SegTree:

    def __init__(self, start, end):
        self.lChild = None
        self.rChild = None
        self.start = start
        self.end = end
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        booking = SegTree(startTime, endTime)
        if not self.root:
            self.root = booking
            return True
        
        curr = self.root


        while curr:
            if curr.end <= startTime:
                if curr.rChild:
                    curr = curr.rChild
                else:
                    curr.rChild = booking
                    return True

            elif curr.start >= endTime:
                if curr.lChild:
                    curr = curr.lChild
                else:
                    curr.lChild = booking
                    return True
            
            else:
                return False




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)