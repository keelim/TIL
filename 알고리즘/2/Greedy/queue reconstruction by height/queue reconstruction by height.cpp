
class Solution {
public:
    struct compare{
      bool operator()(vector<int>&a, vector<int>&b){
        if(a[0]==b[0])
          return a[1]>b[1];
        return a[0]<b[0];
      }
    };
    
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n=people.size();
        priority_queue<vector<int>, vector<vector<int>>> pq;
        vector<vector<int>> ans;
        for(int i=0;i<n;i++){
           pq.push({people[i][0], people[i][1]});
        }
        while(!pq.empty()){
            auto curr=pq.top(); 
            ans.insert(ans.begin()+curr[1], curr);
            pq.pop();
        }
        return ans;
    }
};