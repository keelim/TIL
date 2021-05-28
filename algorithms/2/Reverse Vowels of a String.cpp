#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        string search ="";
        for(auto ele: s){
            if(vowels.find(ele)){
                search+=ele;
            }
        }
        reverse(search.begin(), search.end());
        
        string result = "";
        int i=0;
        for (auto ele : s){
            if(vowels.find(ele) == string::npos){
                result+=ele;
            } else{
                result += search[i];
                i+=1;
            }
        }

        return result;
    }
};