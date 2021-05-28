#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
      string standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      unordered_map<char, int> map;
      for (int i=0; i<standard.size(); i++){
        map[standard[i]] = i+1;
      }
      int result = 0;
      int a = 1;
      while (s.size()>0){
        if(s.size()==1){
          result+=(map[s[0]]*a);
          s="";
        } else{
            result += (map[s[s.size()-1]]*a);
            s = s.substr(0,s.size()-1); 
            a*=26;
        }  
      }
      return result;
      
    }
};