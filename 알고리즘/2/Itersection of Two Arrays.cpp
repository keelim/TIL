#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());

        vector<int> result;
        for(auto ele: set1){
            if(set2.find(ele) != set2.end()){
              result.push_back(ele);
            }
        }

        return result;
    }
};