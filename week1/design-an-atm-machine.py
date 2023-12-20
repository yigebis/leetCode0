class ATM:

    def __init__(self):
        self.amount = {
            20 : 0,
            50 : 0,
            100 : 0,
            200 : 0,
            500 : 0
        }
        self.money = {
            0 : 20,
            1 : 50,
            2 : 100,
            3 : 200,
            4 : 500
        }

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.amount[self.money[i]] += banknotesCount[i]


    def withdraw(self, amt: int) -> List[int]:
        notes = [0,0,0,0,0]
        i = 4
        while i > -1:
            if self.amount[self.money[i]] > 0:
                have = self.amount[self.money[i]]
                notes[i] = min(amt//self.money[i], have)
                amt -= notes[i] * self.money[i]
            i -= 1
        if amt > 0:
            return [-1]
        for j in range(len(notes)):
            self.amount[self.money[j]] -= notes[j]
        return notes

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)