#include <bits/stdc++.h>

using namespace std;

string number_to_n(int num, int n){
    string result;
    string number="0123456789ABCDEF"
    if(num == 0){
        return "0";
    }

    while(num > 0){
        result = number[num % n] + result;
        num /= n;
    }
    return result;
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    string temp;

    int mt = m * t;

    for(int i = 0; temp.size() <= mt; i++){
        string ngame = number_to_n(i, n);
        temp += ngame;
    }

    for(int i = 0; i < t; i++){
        answer += temp.at((m*i)+(p-1));
    }

    return answer;
}