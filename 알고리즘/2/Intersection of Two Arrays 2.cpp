#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map;
        if(nums1.size() < nums2.size()){
            swap(nums1, nums2);
        }

        for(auto ele : nums1){
            map[ele]+=1;
        }
        vector<int> result;
        for (auto ele: nums2){
            if(map[ele]>0){
                map[ele]-=1;
                result.push_back(ele);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};