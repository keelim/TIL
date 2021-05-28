class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(range)):
                for k in range(j+1, len(range)):
                    if arr[i] - arr[j] <= a and arr[j]-arr[k] <=b and arr[i] - arr[k] <= c :
                        count+=1
        return count