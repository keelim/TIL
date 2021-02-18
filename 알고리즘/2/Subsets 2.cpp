#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        int n = nums.size();
        set<vector<int>> set1;
        
        for(int i=0; i<(1<<n); i++){
            vector<int> temp;
            for(int j=0; j<n; j++){
                if( i & (1<<j)){
                    temp.push_back(nums[j]);
                }
            }
            set1.insert(temp);
        }
        vector<vector<int>> result(set1.begin(), set1.end());
        return result;
    }
};