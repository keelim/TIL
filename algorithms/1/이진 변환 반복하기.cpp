#include <bits/stdc++.h>

using namespace std;

string n_to_2(int one){
    string bin;
    while(one>0){
        bin = to_string(one%2)+bin;
        one/=2;
    }
    return bin;
}

vector<int> solution(string s) {
    vector<int> answer;
    
    int i=0;
    int zero = 0;
    while(true){
        i+=1;
        zero+=count(s.begin(), s.end(), '0');
        int one = count(s.begin(), s.end(), '1');

        s = n_to_2(one);
        
        if(s=="1") break;
    }
    answer.push_back(i);
    answer.push_back(zero);
    return answer;
}