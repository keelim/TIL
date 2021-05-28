class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        list =[]
        for i in range(len(a)):
            list.append(a[i])
            list.append(b[i])
        return list