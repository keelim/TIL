#include <vector>

using namespace std;


class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> vc;

        for(int i=0; i<n; i++){
            vc.push_back(nums[i]);
            vc.push_back(nums[i+n]);
        }

        return vc;
    }
};