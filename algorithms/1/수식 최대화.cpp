#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

long long solution(string expression)
{
  long long answer = 0;
  vector<long long> vc;
  vector<char> exp, location;
  string num = "";

  for (char ele : expression)
  {
    if (ele >= '0' && ele <= '9')
      num += ele;

    else
    {
      vc.push_back(stoi(num));
      num = "";

      if (find(exp.begin(), exp.end(), ele) == exp.end())
        exp.push_back(ele);

      location.push_back(ele);
    } // 숫자는 문자열로 하자
  }

  vc.push_back(stoi(num));
  sort(exp.begin(), exp.end());

  do
  {
    vector<long long> temp = vc;
    vector<char> tmp_loc = location;

    for (int i = 0; i < exp.size(); i++)
    {
      for (int j = 0; j < tmp_loc.size(); j++)
      {
        if (exp[i] == tmp_loc[j])
        {
          if (tmp_loc[j] == '+')
            temp[j] += temp[j + 1];

          else if (tmp_loc[j] == '-')
            temp[j] -= temp[j + 1];

          else if (tmp_loc[j] == '*')
            temp[j] *= temp[j + 1];

          temp.erase(temp.begin() + j + 1);
          tmp_loc.erase(tmp_loc.begin() + j);
          j--;
        }
      }
    }

    answer = max(answer, abs(temp[0]));
  } while (next_permutation(exp.begin(), exp.end()));

  return answer;
}