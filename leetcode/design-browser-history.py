class DoubleListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = DoubleListNode(homepage)        

    def visit(self, url: str) -> None:
        temp = DoubleListNode(url)
        self.curr.next = temp
        temp.prev = self.curr
        self.curr = temp

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)