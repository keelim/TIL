#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        unordered_map<int, int> map;
        unordered_set<int> s(nums.begin(), nums.end());

        for(auto ele1 : s){
            for(auto ele2 : nums){
                if(ele2 < ele1) map[ele1]++;
            }
        }

        vector<int> answer;

        for(auto ele : nums){
            answer.push_back(map[ele]);
        }
        
        return answer;    
    }
};