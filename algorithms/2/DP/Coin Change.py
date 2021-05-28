class Solution:
    def coinChange(coins, amount) :
 
    def helper(remain) :
 
        if remain < 0 : return -1
        if remain == 0 : return 0
 
        ans = float("inf")
 
        for coin in coins :
 
            tmp = helper(remain-coin) # 남은 돈 계산
 
            if tmp != -1 :
                ans = min(tmp+1, ans)
 
        return ans if ans != float("inf") else -1       
    
    return helper(amount)
    
coinChange([5000, 1000, 500, 100], 5900)
        