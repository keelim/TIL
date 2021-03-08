#include <bits/stdc++.h>

using namespace std;

int solution(int n) {

    string s= bitset<32>(n).to_string();
    int one = 0;
    one = count(s1.begin(), s1.end(), '1')
    int answer = 0;

    for(int i = n+1;;i++){
        string s2 = bitset<32> (i).to_string();
        int two  = count(s2.begin(), s2.end(), '1');
        
        if(one==two){
            return i;
        }
    }
}