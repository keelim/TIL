class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer =[0];
        pointer = 0
        
        for ele in gain:
            pointer+=ele
            answer.append(pointer)
        return max(answer)
        
    def largestAltitude2(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))