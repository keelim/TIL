#include <bits/stdc++.h>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> map;

    for(auto ele : participant){
        if(map.find(ele)==map.end()){
            map.insert({ele, 1});
        } else{
            map[ele]+=1;
        }
    }

    for(auto ele: completion){
        map[ele]-=1;
    }

    for(auto ele : participant){
        if(map[ele]>0) return ele;
    }
}