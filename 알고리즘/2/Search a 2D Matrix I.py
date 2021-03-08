class Solution:
    def binary_search(self, arr1, target, left, right):

        while left <= right:
            mid = left + (right-left)//2
            if arr1[mid] == target:
                return mid
            elif target < arr1[mid]:
                right = mid-1
            elif arr1[mid] < target:
                left = mid+1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target <= i[-1]:
                if -1 < self.binary_search(i, target, 0, len(i)):
                    return True
        return False
