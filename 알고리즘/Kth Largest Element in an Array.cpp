
#include <vector>
#include <queue>
#include <set>


using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int> pq; //max heap
        for(auto ele : nums)  {
            pq.push(ele);
        }

        for(int i=0; i<k-1; i++) pq.pop();

        return pq.top();
    }
};