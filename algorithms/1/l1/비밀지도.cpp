#include <bits/stdc++.h>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    for (int i=0; i<n; i++){
      auto a = bitset<16> (arr1[i]|arr2[i]).to_string();
      auto a1 = a.substr(distance(a.begin(), a.end()-n), n);
      replace(a1.begin(), a1.end(), '1', '#');
      replace(a1.begin(), a1.end(), '0', ' ');
      answer.push_back(a1);
    }
    return answer;
}