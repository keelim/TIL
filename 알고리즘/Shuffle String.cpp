#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        unordered_map<int, char> map;
        for(int i=0; i<s.size(); i++){
            map.insert({indices[i], s[i]});
        }
        string temp;
        for(int i=0; i<s.size(); i++){
            temp+=map[i];
        }
        return temp;
    }
    
    string restoreString2(string s, vector<int>& indices) {
        string res = s;
        for(int i =0; i < indices.size(); ++i)
            res[indices[i]] = s[i];
        return res;
    }