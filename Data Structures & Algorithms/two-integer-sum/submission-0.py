class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in map:
                return [map[val], i]
            map[nums[i]] = i
        

                
        