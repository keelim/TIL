#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string thousandSeparator(int n) {
        if(n==0) return "0";
        int i = 0;

        string result ="";
        for(int i=0; n>0; i++){
          if(i%3==0 && i!=0){
            result = "." +result;
          }
          result += to_string(n%10);
          n/=10;
        }
        return result;
    }
};