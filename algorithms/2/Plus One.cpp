#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        string s1;
        for(auto ele : digits) {
            s1+=ele;
        }
        int a  = stoi(s1)+1;
        vector<int> result;
        
        while (a>0){
            if(result.empty()){
                result.push_back(a%10);
                a/=10;
            } else{
                result.insert(result.begin(), a%10);
                a/=10;
            }
        }
        return result;
    }
};