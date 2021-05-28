class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        dict1 = dict()

        for ele in set1:
            for ele1 in nums:
                dict1[ele1] = dict1.get(ele1, 0) + 1
        
        return [dict1.get(ele) for ele in nums ]
        