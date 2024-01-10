class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true_max, false_max = 0, 0
        falses, trues = 0, 0
        l = 0

        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                falses += 1
            while falses > k:
                if answerKey[l] == 'F':
                    falses -= 1
                l += 1
            true_max = max(true_max, r - l + 1)
        
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                trues += 1
            while trues > k:
                if answerKey[l] == 'T':
                    trues -= 1
                l += 1
            false_max = max(false_max, r - l + 1)
        return max(true_max, false_max)
