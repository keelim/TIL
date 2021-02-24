#include <bits/stdc++.h>
using namespace std;

// class Solution:
//     def binary_search(self, arr1, target, left, right):

//         while left <= right:
//             mid = left + (right-left)//2
//             if arr1[mid] == target:
//                 return mid
//             elif target < arr1[mid]:
//                 right = mid-1
//             elif arr1[mid] < target:
//                 left = mid+1

//         return -1

//     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
//         for i in matrix:
//             if i[0] <= target <= i[-1]:
//                 if -1 < self.binary_search(i, target, 0, len(i)):
//                     return True
//         return False
class Solution
{
public:
    int binary_search(vector<int> &line, int target, int left, int right)
    {
        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (line[mid] == target)
            {
                return mid;
            }
            else if (target < line[mid])
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return -1;
    }

    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int n = matrix.size();
        int m = matrix[0].size();

        for (int i = 0; i < n; i++)
        {
            if (matrix[i][0] <= target && target <= matrix[i][m - 1])
            {
                if (binary_search(matrix[i], target, 0, m) > -1)
                return true;
            }
        }
        return false;
    }
};