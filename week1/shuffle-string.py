class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp_arr = [0]* len(s)
        for i in range(len(indices)):
            temp_arr[indices[i]] = s[i]
        return "".join(temp_arr)