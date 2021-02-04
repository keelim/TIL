#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string basic = "aeiouAEIOU";
    int cnt(string s){
      int count = 0;
      for(auto ele : s){
        if(basic.find(ele)!=string::npos) count+=1;
      }
      return count;
    }

    bool halvesAreAlike(string s) {
      
      string a, b;

      for (int i = 0; i < s.size(); i++)
      {
        if(i<s.size()/2){
          a+=s[i];
        } else{
          b+=s[i];
        }
      }
      int acount = cnt(a);
      int bcount = cnt(b);

      return acount==bcount;
    }
};