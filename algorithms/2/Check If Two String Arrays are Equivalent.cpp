class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string a;
        for (auto ele1: word1){
            a+=ele1;
        }
        
        string b;
        
        for(auto ele2: word2){
            b+=ele2;
        }
        
        
        return a==b;
    }
};