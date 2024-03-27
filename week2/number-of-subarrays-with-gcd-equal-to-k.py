class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                gcd = math.gcd(nums[j], gcd)
                if gcd == k:
                    count += 1
                elif nums[j] % k != 0:
                    break
        
        return count
        

        # if k == 1:
        #     return (len(nums) * (len(nums) - 1))//2
        # pre_sum = []
        # if nums[0] == k:
        #     pre_sum.append(1)
        # else:
        #     pre_sum.append(0)
        # one_found = False
        # l = 0
        # for r in range(1, len(nums)):
        #     if nums[r] == k == 1:
        #         pre_sum.append(pre_sum[-1] + r + 1)
        #         one_found = 
        #         continue
        #     if math.gcd(nums[r], nums[r-1]) == k:
        #         pre_sum.append(pre_sum[-1] + r - l) 
        #     else:
        #         pre_sum.append(pre_sum[-1])
        #         l = r
        #     if nums[r] == k:
        #         pre_sum[-1] += 1
        
        # return pre_sum[-1]