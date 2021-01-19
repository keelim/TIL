class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int rich = 0;
        for(auto person : accounts){
            int a = 0;
            for(auto money : person) a+=money;
            rich = max(rich, a);
        }
        
        return rich;
    }
};