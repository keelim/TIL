class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = list(map(str, digits))
        s1 = ''.join(list1)
        s1+='+1'
        return list(str(eval(s1)))
        