class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # have a pointer 
        # check if the character at that pointer is common to all strings
        # if yes, increment the pointer
        # if no, 
        #   if the pointer is 0, return ""
        #   else return a slice of one of the strings from 0 to that ptr
        pointer = 0
        min_length = 200
        for i in strs:
            min_length = min(min_length, len(i))
        while pointer < min_length:
            comp_char = strs[0][pointer]
            for i in range(1, len(strs)):
                if strs[i][pointer] != comp_char:
                    # if pointer == 0:
                    #     return ""
                    return strs[0][0:pointer]
            pointer += 1
        return strs[0][0:pointer]