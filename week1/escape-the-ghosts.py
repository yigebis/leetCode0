class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # first find the #of steps you need to reach the target 
        # iterate through the array and check if there is a ghost who can reach
        # the destination with less or equal steps than you
        # if so return false
        # after finishing iteration, return true

        my_steps = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            ghost_steps = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_steps <= my_steps:
                return False
        
        return True