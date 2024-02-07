class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0 for i in range(len(s) + 1)]
        s_arr = [(ord(s[i]) - 97) for i in range(len(s))]
        for s in shifts:
            if s[2] == 0:
                arr[s[0]] -= 1
                arr[s[1] + 1] += 1
            else:
                arr[s[0]] += 1
                arr[s[1] + 1] -= 1
        for i in range(1, len(arr) - 1):
            arr[i] += arr[i-1]
        for i in range(len(s_arr)):
            s_arr[i] += arr[i]
            s_arr[i] %= 26
        for i in range(len(s_arr)):
            s_arr[i] = chr(s_arr[i] + 97)
        return "".join(s_arr)



        