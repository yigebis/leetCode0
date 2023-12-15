class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = []
        index_sum = 0
        ones_before = [0 for i in range(len(boxes))]
        summer = 0
        total = 0

        for i in range(len(boxes)):
            if boxes[i] == "1":
                index_sum += i
        ones_before[0] = 0
        if boxes[0] == "1":
            summer = 1
        for i in range(1, len(boxes)):
            ones_before[i] = summer + ones_before[i-1]
            if boxes[i] == "1":
                summer += 1
        
        print(ones_before)
        for i in range(len(boxes)):
            operations.append(index_sum + 2*ones_before[i])
            index_sum -= summer

        return operations
