#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  int lengthOfLongestSubstring(string s)
  {
    unordered_map<char, int> used; // 해시를 하나 지정을 해준다

    int start = 0;
    int max_length = 0;

    for (auto i = 0; i < s.size(); i++) //char 를 돌면서
    {
      char ele = s[i];
      if (used.find(ele) != used.end() && start <= used[ele]) // 해시 안에 있고 start 가 짧다면
      {
        start = used[ele] + 1; // start 갱신
      }
      else // 아니면
      {
        max_length = max(max_length, i - start + 1); //max 값 갱신
      }
      used[ele] = i; //index를 넣어준다.
    }
    return max_length; // 최댓값 반환
  }
};