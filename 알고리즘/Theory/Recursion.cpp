#include <bits/stdc++.h>
//
using namespace std;

int sum(int n)
{
  int result;
  for (int i = 1; i <= n; i++)
  {
    result += i;
  }
  return result;
}

int recursiveSum(int n)
{
  if (n == 1)
    return 1;
  return n + recursiveSum(n - 1);
}

// n개의 원소 중 m 개를 고르는 모든 조합을 찾는 알고리즘

void pick(int n, vector<int> &picked, int toPick)
{
  if (toPick == 0)
  {
    printPicked(picked);
    return;
  }

  int smallest = picked.empty() ? 0 : picked.back() + 1;

  for (int next = smallest; next < n; next++)
  {
    picked.push_back(next);
    pick(n, picked, toPick - 1);
    picked.pop_back();
  }
}

int dx[] = {-1, -1, -1, 1, 1, 1, 0, 0};
int dy[] = {-1, 0, 1, -1, 0, 1, -1, 1};

bool hasWord(int y, int x, string word){
  //x, y 범위 넘어서면
  if(!inRange(y, x)) return false;
  // 글자가 다르면
  if(board[y][x]!=word[0]) return false;

  if(word.size()==1) return true;

  for(int i=0; i<8; i++){
    int nx = x+dx[i], ny = y+dy[i];

    if(hasWord(ny, nx, word.substr(1))) return true;

    return false;
  }



}

int main(int argc, char const *argv[])
{
  /* code */
  return 0;
}
