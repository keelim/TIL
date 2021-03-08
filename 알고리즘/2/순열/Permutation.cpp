#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> answer;
        do{
            answer.push_back(nums);
        } while (next_permutation(nums.begin(), nums.end()));
        return answer;
    }
};