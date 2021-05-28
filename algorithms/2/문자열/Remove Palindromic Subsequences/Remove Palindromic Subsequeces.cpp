#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int removePalindromeSub(string s) {
        if (s.size()==0) return 0;
        string re(s.rbegin(), s.rend());
        if (s==re) return 1;
        return 2;        
    }
};