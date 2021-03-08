class Solution:
    def maxArea(self, height):
        max_value = 0
        left = 0
        right = len(height) - 1
        while right != left:

            if height[right] > height[left]:
                value = height[left] * (right - left)
                left += 1
            else:
                value = height[right] * (right - left)
                right -= 1

            max_value = max(max_value, value)
        return max_value
