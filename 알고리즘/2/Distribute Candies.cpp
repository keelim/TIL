#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> set1(candyType.begin(), candyType.end());
        return min(set1.size(), candyType.size()/2);
    }
};