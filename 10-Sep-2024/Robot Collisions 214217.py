# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        remaining = []
        stack = []
        for i in range(len(positions)):
            positions[i] = [positions[i], i]
        
        positions.sort()
        # print(positions)

        for i in range(len(positions)):
            pos, ind = positions[i]
            # print(ind)
            if directions[ind] == "L" and not stack:
                remaining.append((ind, healths[ind]))
                continue
            elif directions[ind] == "R":
                stack.append(ind)
            else:
                prev_ind = stack.pop()
                while healths[prev_ind] < healths[ind]:
                    healths[ind] -= 1
                    healths[prev_ind] = 0
                    if healths[ind] == 0:
                        break
                    if not stack:
                        remaining.append((ind, healths[ind]))
                        break
                    prev_ind = stack.pop()
                
                if healths[prev_ind] > healths[ind]:
                    healths[prev_ind] -= 1
                    if healths[prev_ind] > 0:
                        stack.append(prev_ind)

                else:
                    continue
        
        
        # print(stack)
        for ind in stack:
            remaining.append((ind, healths[ind]))
        
        remaining.sort()
        for i in range(len(remaining)):
            remaining[i] = remaining[i][1]
            
        return remaining
                