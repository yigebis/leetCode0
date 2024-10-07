# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not(start >= e or s >= end):
                return False
            
        for s, e in self.non_overlapping:
            if not(start >= e or s >= end):
                self.overlapping.append((max(s, start), min(e, end)))
        
        self.non_overlapping.append((start, end))

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)