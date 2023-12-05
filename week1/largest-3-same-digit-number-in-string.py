class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num += "a"
        number = -1

        for i in range(len(num) - 3):
            if num[i] == num[i + 1] == num[i + 2] != num[i + 3]:
                number = max(number, int(num[i]))
        if number == -1 :
            return ""
        return str(number) * 3