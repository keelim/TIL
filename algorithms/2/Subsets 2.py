class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        set1 = set()
        for i in range((1<<n)):
            temp =[]
            for j in range(n):
                if i & (1<<j):
                    temp.append(nums[j])
                temp.sort()
                
            set1.add(temp)
        return list(set1)
            