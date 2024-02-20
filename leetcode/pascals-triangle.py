class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        def pascal(self, rowIndex):
            if rowIndex == 0:
                return [1]

            prev_row = pascal(self,rowIndex - 1)
            ans.append(prev_row)
            print(numRows, ans)
            arr = [1]

            for i in range(rowIndex - 1):
                arr.append(prev_row[i] + prev_row[i+1])
            arr.append(1)

            return arr
        arr = pascal(self,numRows - 1)
        print(arr)
        ans.append(arr)
        return ans