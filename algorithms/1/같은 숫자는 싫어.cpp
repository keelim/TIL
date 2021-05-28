#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr){
    vector<int> answer;

    if(arr.size()==1) return arr;

    int before = arr[0];

    for(auto ele : arr){
        if(answer.empty()) {
            answer.push_back(ele);
            continue;
        }

        if(ele!=before){
            answer.push_back(ele);
            before = ele;
            continue;
        }
    }

    return answer;
}