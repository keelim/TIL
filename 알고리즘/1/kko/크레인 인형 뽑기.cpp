#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves)
{
    int answer = 0;
    for (int i = 0; i < moves.size(); i++)
    {
        moves[i] -= 1;
    }
    stack<int> stack;

    for (auto command : moves)
    {
        for (int i = 0; i < board.size(); i++)
        {
            if (board[i][command] != 0)
            {
                stack.push(board[i][command]);
                board[i][command] = 0;
                break;
            }
        }

        if (stack.size() >= 2)
        {
            auto a = stack.top();
            stack.pop();
            auto b = stack.top();
            stack.pop();

            if (a == b)
            {
                answer += 2;
            }
            else
            {
                stack.push(a);
                stack.push(b);
            }
        }
    }

    return answer;
}