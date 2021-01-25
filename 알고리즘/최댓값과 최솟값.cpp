#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> vc;
    s+='\n';
    for (int i = 0; i < s.size(); i++) {
        if(s[i]==' '||s[i]=='\n'){
            vc.push_back(stoi(answer));
            answer.clear();
        }
        answer.push_back(s[i]);
    }

    int min = *min_element(vc.begin(), vc.end());
    int max = *max_element(vc.begin(), vc.end());
    
    return to_string(a.first)+ " "+to_string(a.second);
}