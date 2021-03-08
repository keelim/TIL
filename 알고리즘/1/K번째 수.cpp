#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(auto ele : commands){
        vector<int> temp;
        temp.assign(array.begin() + ele[0] - 1, array.begin() + ele[1]);
        sort(temp.begin(), temp.end());
        answer.push_back( temp[ele[2] - 1]);
    }

    return answer;
}