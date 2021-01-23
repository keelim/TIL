class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        if(s.size()!=t.size()) return false;
        
        for(int i=0; i<s.size(); i++){
            if(s[i]!=t[i]) return false;
        }
        
        return true;
        
    }

    bool isAnagram2(string s, string t){
        if(s.size()!=t.size()) return false;

        int counter[26] = {0,};

        for(int i=0; i<s.size(); i++){
            counter[s[i]-'a']+=1;
            counter[t[i]='a']-=1;
        }

        for(auto ele : counter){
            if(ele!=0) return false;
        }
        
        return true;
    }
};