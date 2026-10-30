class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for a in nums:
            if a in hashset:
                return True
            hashset.add(a) 
        return False