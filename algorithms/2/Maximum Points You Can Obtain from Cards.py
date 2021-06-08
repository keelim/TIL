class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        f = [0]*len(cardPoints)
        f[0] = cardPoints[0]
        f[1] = cardPoints[1]

        for i in range(2, len(cardPoints)):
            f[i] = cardPoints[i]+min(f[i-1], f[i-2])
    