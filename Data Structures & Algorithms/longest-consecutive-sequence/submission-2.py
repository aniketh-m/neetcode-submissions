class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        longest = 0

        for i in l:
            if i - 1 not in l:
                length = 1
                while i + length in l:
                    length += 1
                longest = max(longest, length)

        return longest

        