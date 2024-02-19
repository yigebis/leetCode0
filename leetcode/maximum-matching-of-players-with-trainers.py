class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0                     
        count = 0
        
        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                i += 1
                count += 1
            j += 1
        return count