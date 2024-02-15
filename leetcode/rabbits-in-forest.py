class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        min_rabits = 0

        answers.sort()
        min_rabits = answers[0] + 1
        others = answers[0]

        for i in range(1, len(answers)):
            if answers[i] == answers[i-1] and others > 0:
                others -= 1
                continue
            min_rabits += answers[i] + 1
            others = answers[i]
        
        return min_rabits
