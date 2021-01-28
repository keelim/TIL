#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer = arr;
    if (arr.size() == 1) return { -1 };
    else {
        int pointer = *min_element(answer.begin(), answer.end());
        answer.erase(std::remove(answer.begin(), answer.end(), pointer), answer.end());
        return answer;
    }
}