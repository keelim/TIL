#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    string s;
    
    while (n>0){
        s = to_string(n%3) +s;
        n = n/3;
    }
    reverse(s.begin(), s.end());
    
    int a = 0;
    int b = 1;
    for(int i=s.size()-1; i>=0; i--){
        a += (s[i]-'0')*b;
        b*=3;
    }

    return a;
}