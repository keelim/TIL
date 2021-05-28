#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<string>> clothes)
{
    int answer = 1;
    unordered_map<string, int> data;
    for (auto clothe : clothes)
    {
        data[clothe[1]] += 1;
    }

    for (auto it = data.begin(); it != data.end(); it++)
    {
        answer *= it->second + 1;
    }
    answer-=1;
    return answer;
}