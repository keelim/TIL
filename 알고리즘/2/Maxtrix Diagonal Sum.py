class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        o = len(mat)
        sum = 0
        for ele in range(o):
            sum += mat[ele][ele]
            sum += mat[ele][o-ele-1]
        return sum - mat[o//2][o//2] if o&1 else sum