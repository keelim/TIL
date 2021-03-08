#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int countConsistentStrings(string allowed, vector<string> &words)
    {
        int count = 0;
        for(auto ele1: words){
            unordered_set<char> set(ele1.begin(), ele1.end());

            for(auto ele2 : set){
                if(allowed.find(ele2)==string::npos){
                    count+=1;
                    break;
                }
            }
        }
        return words.size() - count;
    }

     int countConsistentStrings2(string allowed, vector<string>& words) {
        // support variable
        int res = words.size();
        unordered_set<char> set;
        // populating alpha
        for (char c: allowed) set.insert(c);
        // parsing all the words to see if each character is in alpha
        for (string word: words) {
            // in case we find an unallowed character, we decrease res and break
            for (char c: word) if (set.find(c)==set.end()) {
                res--;
                break;
            }
        }
        return res;
    }
};