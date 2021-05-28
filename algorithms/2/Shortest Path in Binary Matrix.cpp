#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int visited[101][101];

    int bfs(vector<vector<int>> grid)
    {
        int dx[] = {1, -1, 0, 0, 1, 1, -1, -1};
        int dy[] = {0, 0, 1, -1, 1, -1, 1, -1};
        
        int n = grid.size();
        queue<tuple<int, int, int>> q;
        q.push({0, 0, 1});
        visited[0][0] = 1;

        while (!q.empty())
        {
            int x, y, cnt;
            tie(x, y, cnt) = q.front();
            q.pop();

            if (x == n - 1 && y == n - 1)
            {
                return cnt;
            }

            for (int i = 0; i < 8; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue;

                if (grid[nx][ny] == 0 && visited[nx][ny] == 0)
                {
                    q.push({nx, ny, cnt + 1});
                    visited[nx][ny] = 1;
                }
            }
        }
        return -1;
    }

    int shortestPathBinaryMatrix(vector<vector<int>> &grid)
    {
        if (grid[0][0] == 1 || grid[grid.size() - 1][grid.size() - 1] == 1)
            return -1;

        return bfs(grid)
    }
};