class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if(n==0): return 0
        if(n==1): return 1

        list =[]
        list.append(0)
        list.append(1)

        for i in range(1, int(n/2)+1):
            list.append(list[i])
            list.append(list[i] + list[i+1])
        
        return max(list[:n+1])
        