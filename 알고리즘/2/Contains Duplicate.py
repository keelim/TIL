class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for ele in nums:
            if(len(s)==0):
                s.add(ele)
                continue
            
            if(ele not in s):
                s.add(ele)
            else:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        s = set(nums)
        return True if len(s)!=len(nums) else False