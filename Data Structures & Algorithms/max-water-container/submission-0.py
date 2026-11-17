class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_area = 0
        j = len(heights) - 1
        i = 0

        while i < j:
            width = j - i
            total = width * min(heights[i], heights[j])
            largest_area = max(largest_area, total)

            if heights[i] < heights[j]:
                i += 1

            else:
                j -= 1

        return largest_area
            