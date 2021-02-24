class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0

        if X > Y:
            return X-Y

        if Y % 2 == 0:
            return 1+self.brokenCalc(X, Y//2)

        else:
            return 1+self.brokenCalc(X, Y+1)
