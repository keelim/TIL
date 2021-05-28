#include <bits/stdc++.h>

using namespace std;
class Solution
{
public:
    int longestPalindrome(string s)
    {
        unordered_map<char, int> map;

        for (auto ele : s)
        {
            map[ele] += 1;
        }

        int cnt = 0;

        bool flag = false;
        for (auto iter = map.begin(); iter!=map.end(); iter++){
            cnt+=(iter->second/2)*2;
            if (iter->second %2 ==1) flag = true;
        }

        if(flag){
            cnt+=1;
        }
        return cnt;
    }
};