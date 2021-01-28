class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int a = 0;
        int b = 0;
        int result = 0;
        for(int i=0; i<nums.size(); i++){
            a = nums[i];
            for(int j=i+1; j<nums.size(); j++){
                b = nums[j];
                if(a==b) result +=1;
            }
        }
        return result;
    }
};