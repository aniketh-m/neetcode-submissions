class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        running = 1
        for i in range(n):
            res[i] = running
            running *= nums[i]
        
        running = 1
        for i in range(n-1, -1, -1):
            res[i] *= running
            running *= nums[i]

        return res



        
        