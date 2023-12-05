class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # keep track of the current capacity we have
        # also keep track of the total steps
        # iterate through the array upto the one before the last
            # decrement the current capacity by the element at the current index
            # check if current capacity >= the next element
            # if true: keep decrementing 
            # else: add two times (current index + 1) to the total steps
            #     : make current capacity equal to capacity
        # finally increment the length of plants to the total steps

        current_capacity = capacity
        total_steps = 0
        
        for i in range(len(plants) - 1):
            current_capacity -= plants[i]
            if current_capacity < plants[i + 1]:
                total_steps += 2 * (i + 1)
                current_capacity = capacity
        
        total_steps += len(plants)

        return total_steps