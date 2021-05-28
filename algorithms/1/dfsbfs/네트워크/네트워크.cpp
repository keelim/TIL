#include <bits/stdc++.h>

using namespace std;
vector<int> visited;
void bfs(int node, vector<vector<int>> computers)
{
    queue<int> q;
    q.push(node);
    visited[node] = 1;

    while (!q.empty())
    {
        auto x = q.front();
        q.pop();

        for (int i = 0; i < computers[x].size(); i++)
        {
            if (visited[i] == 0 && computers[x][i] == 1)
            {
                q.push(i);
                visited[i] == 1;
            }
        }
    }
}

int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;
    visited = vector<int>(n, 0);
    for (int i = 0; i < n; i++)
    {
        if (visited[i] == 0)
        {
            answer += 1;
            bfs(i, computers);
        }
    }

    return answer;
}