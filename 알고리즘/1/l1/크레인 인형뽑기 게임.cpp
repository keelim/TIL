#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> stack;
    int n = board.size();

    for(auto move: moves){
        int idx = move-1;
        for(int i=0; i<n; i++){
            if(board[i][idx]!=0){
                stack.push_back(board[i][idx]);
                board[i][idx] = 0;
                break;
            }
        }
        
        if(stack.empty() || stack.size()==1) continue;
        else if (stack[stack.size()-1] == stack[stack.size()-2]){
            stack.erase(stack.end()-1);
            stack.erase(stack.end()-1);
            answer+=2;
        } 
    }
    return answer;
}