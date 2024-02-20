class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev_row = self.getRow(rowIndex - 1)
        arr = [1]

        for i in range(rowIndex - 1):
            arr.append(prev_row[i] + prev_row[i+1])
        arr.append(1)

        return arr