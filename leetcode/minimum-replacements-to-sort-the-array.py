class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        min_operations = 0
        min_right = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            spaces = ceil(nums[i] / min_right)
            # eg 3 10 3 , for 10, we need 
            # ceil(3.3) = 4 spaces minimum

            greedy_num = nums[i] // spaces
            # eg. 2 10 3 => I know I have to choose 4 spaces. But, I can fill those spaces with different arrangements
            # one of them can be like 1 3 3 3. But, I can make it like 2 2 3 3, and it is better
            # since I would have 2 [2 2 3 3] 3 requiring no more operations.
            # And, can I make the number more than 2? No. take 3 for example, 3 3 3 3 will make it 12 > 10
            # So, what is so special about 2? 10 // (spaces = 4) = 2.
            # 10 divided by the total number of spaces = 4, each space receives at least 2
            # Then, for the last numbers, we can add the modulo
            
            min_right = greedy_num
            min_operations += spaces - 1
        return min_operations

            