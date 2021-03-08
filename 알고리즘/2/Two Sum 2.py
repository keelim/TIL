class Solution:
    def twoSum1(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
 
# dictionary           
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
 
# binary search        
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right-left)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    left = mid+1
                else:
                    right = mid-1
            
            