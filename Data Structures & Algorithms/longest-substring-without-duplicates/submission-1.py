class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            best = max(best, (r - l) + 1)
            
        return best
 


            
