#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int x = 0;
        int y = matrix[0].size() - 1;
        int n = matrix.size();
        while (y >= 0 and x < n)
        {
            if (matrix[x][y] > target)
                y -= 1;
            else if (matrix[x][y] < target)
                x += 1;
            else
                return true;
        }
        return false;
    }
};