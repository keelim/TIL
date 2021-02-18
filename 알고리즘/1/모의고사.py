#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> first = {1, 2, 3, 4, 5};
    vector<int> second = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    int fcnt = 0;
    int scnt = 0;
    int tcnt = 0;

    for (int i = 0; i < answers.size(); i++) {
        int a = i % first.size();
        int b = i % second.size();
        int c = i % third.size();

        if (first[a] == answers[i])fcnt++;
        if (second[b] == answers[i]) scnt++;
        if (third[c] == answers[i]) tcnt++;
    }

    vector<int> temp = {fcnt, scnt, tcnt};

    int max = *max_element(temp.begin(), temp.end());
    int i=0;
    for(auto ele : temp){
        if(ele == max) answer.push_back(i+1);
        i+=1;
    }

    return answer;
}


