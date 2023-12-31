class Robot:
    def __init__(self, width: int, height: int):
        self.dir = "East"
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.pos = 0

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % (2*(self.width + self.height) - 4)
        if self.pos == 0:
            self.dir = "South"
            self.x = 0
            self.y = 0
        elif self.pos < self.width:
            self.dir = "East"
            self.x = self.pos
            self.y = 0
        elif self.pos < self.width + self.height - 1:
            self.dir = "North"
            self.x = self.width - 1
            self.y = self.pos - self.width + 1
        elif self.pos < 2 * self.width + self.height - 2:
            self.dir = "West"
            self.x = 2 * self.width + self.height - 3 - self.pos
            self.y = self.height - 1
        else:
            self.dir = "South"
            self.x = 0
            self.y = 2 * self.width + 2 * self. height - 4 - self.pos
    def getPos(self) -> List[int]:
        return self.x, self.y

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()