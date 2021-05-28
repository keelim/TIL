#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  int maxProfit(vector<int> &prices)
  {
    int result = 0;
    for (int i = 0; i < prices.size() - 1; i++)
    {
      if (prices[i] < prices[i + 1])
      {
        result += prices[i + 1] - prices[i];
      }
    }
    return result;
  }
};