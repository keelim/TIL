class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        list = sorted(nums)
        print(list)
        return nums[-k]