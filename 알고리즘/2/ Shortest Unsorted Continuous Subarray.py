class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        size = len(nums)

        left = 0
        right = 0
        size -= 1

        # 첫번 째 다른 부분을 찾자
        while left < size - 1 and nums[left] <= nums[left+1]:
            left += 1

        # array is sorted
        if left == size - 1:
            return 0

        # 마지막 다른 부분을 찾자
        while right > 0 and nums[right-1] <= nums[right]:
            right -= 1

        # 제일 큰 원소, 제일 작은 원소를 찾아서
        min_ele = min(nums[left:right+1])
        max_ele = max(nums[left:right+1])

        # 그 부분 까지 포인터를 이동
        while left > 0 and nums[left - 1] > min_ele:
            left -= 1

        # 그 분까지 포인터를 이동
        while right < size - 1 and nums[right+1] < max_ele:
            right += 1

        
        return right - left + 1
