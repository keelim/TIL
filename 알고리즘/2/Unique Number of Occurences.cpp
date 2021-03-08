#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> map;
        for(auto ele : arr){
            map[ele]+=1;
        }

        vector<int> result;

        for (auto iter = map.begin(); iter !=map.end(); iter++){
            if(result.empty()){
                result.push_back(iter->second);
                continue;
            }

            if(find(result.begin(), result.end(), iter->second)!=result.end()){
                return false;
            }

            result.push_back(iter->second);
        }

        return true;
    }
};