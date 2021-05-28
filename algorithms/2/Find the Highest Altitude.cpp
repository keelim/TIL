#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int pointer = 0;
        vector<int> a;
        a.push_back(0);
        for(auto ele : gain){
            pointer+=ele;
            a.push_back(pointer);
        }
        return *max_element(a.begin(), a.end());
    }   
};