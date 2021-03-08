class Solution:
    def __init__(self) -> None:
        self.answer = []

    def go(self, cnt: int, nums, sel, visited):
        global answer
        if cnt == len(nums):
            self.answer.append(sel[:])
            return

        for ele in range(len(nums)):
            if visited[ele] == 0:
                visited[ele] = 1
                sel.append(nums[ele])
                self.go(cnt+1, nums, sel, visited)
                sel.pop()
                visited[ele] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [0]*len(nums)
        sel = []
        self.go(0, nums, sel, visited)
        return self.answer

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        answer = []
        for ele in list(permutations(nums)):
            answer.append(list(ele))
        return set(answer
    