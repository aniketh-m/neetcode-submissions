class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies using a hash map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Step 2: Create a bucket array where the index matches the frequency
        # Length is len(nums) + 1 to account for 0 to n occurrences
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        # Step 3: Iterate backwards from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res