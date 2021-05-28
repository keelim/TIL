#include<bits/stdc++.h>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    auto iter = find(seoul.begin(), seoul.end(), "Kim") -seoul.begin();
    
    answer = "김서방은 "+to_string(iter)+"에 있다";
    
    return answer;
}