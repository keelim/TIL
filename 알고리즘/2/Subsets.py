class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result =[]
        for i in range(0, 1<<n):
            temp =[]
            for j in range(n):
                if i & (1<<j):
                    temp.append(nums[i])
            result.append(temp)

        return result
        