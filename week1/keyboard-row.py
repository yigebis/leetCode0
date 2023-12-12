class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        row_words = []
        
        def row(ch):
            if ch in first_row:
                return first_row
            if ch in second_row:
                return second_row
            return third_row

        for word in words:
            possible_row = row(word[0].lower())
            print(possible_row)
            status = True
            for ch in word:
                if ch.lower() not in possible_row:
                    status = False
                    break
            if status:
                row_words.append(word)
        return row_words