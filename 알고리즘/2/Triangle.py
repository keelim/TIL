class Solution:
    def __init__(self) -> None:
        self.result = 987654321
    def go(self, index:int, position:int,  total:int, triangle) -> None:

        if total > self.result:
            return 

        if index == len(triangle):
            self.result = min(self.result, total)
            return 

        if index < len(triangle)-1:
            self.go(index+1, position, total+triangle[index+1][position], triangle)

            self.go(index+1, position+1, total+triangle[index][position+1], triangle)
        


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        self.go(0, 0, triangle[0][0], triangle)
        return self.result