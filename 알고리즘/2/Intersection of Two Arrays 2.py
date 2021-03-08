
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        dict1 = {}
        for ele in nums1:
            dict1[ele] = dict1.get(ele, 0) + 1
        result = []
        for ele in nums2:
            if(dict1.get(ele, 0)!=0):
                dict1[ele]-=1
                result.append(ele)
        
            
        return sorted(result)


