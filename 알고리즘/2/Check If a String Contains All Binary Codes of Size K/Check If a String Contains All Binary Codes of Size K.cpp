#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> uset;

        for (int i=0; i<s.size()-k+1; i++){
            string temp;
            for(int j=i; j<i+k; j++){
                temp+=s[j];
            }
            uset.insert(temp);
        }
        
        auto a=1;
        for(int i=0; i<k; i++){
            a*=2;
        }

        return uset.size()==a;
    }
};