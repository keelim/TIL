#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    string freqAlphabets(string s)
    {
        string stand = "abcdefghijklmnopqrstuvwxyz";
        unordered_map<int, string> map;

        for (int i = 0; i < 26; i++)
        {
            map.insert({i + 1, to_string(stand[i])});
        }
        string result = "";
        for (int i = 0; i < s.size(); i++)
        {
            if(i+2<s.size()){
                if(s[i+2]=='#'){
                    result += map[stoi(s.substr(i, 2))];
                    continue;
                }
            }

            if(i+1<s.size()){
                if(s[i]=='#' || s[i+1]=='#'){
                    continue;
                }
            }
            
            result += map[s[i]-'0'];
        }
        return result;
    }
};