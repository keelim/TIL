#include <bits/stdc++.h>
using namespace std;

int maxArea(vector<int> &height)
{
    int left = 0;
    int right = height.size() - 1;
    int max_value = 0;

    while (right != left)
    {
        int value = 0;
        if (height[right] > height[left])
        {
            value = height[left] * (right - left);
            left += 1;
        }
        else
        {
            value = height[right] * (right - left);
            right -= 1;
        }
        max_value = max(max_value, value);
    }

    return max_value;
}