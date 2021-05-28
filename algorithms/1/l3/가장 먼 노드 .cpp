#include <vector>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

vector<int> map[20010];
int dist[20010];

int bfs()
{
    memset(dist, -1, sizeof(dist));
    int max_value = 0;
    queue<pair<int, int>> q;
    q.push({1, 0});
    dist[1] = 0; //거리를 이용하여 bfs 를 한다. dist 를 사용할 경우 visited 배열이 필요가 없다.
    while (!q.empty())
    {
        int x, value;
        tie(x, value) = q.front();
        q.pop();
        for (auto nx : map[x])
        {
            if (dist[nx] == -1)
            {
                dist[nx] = value + 1;
                q.push({nx, value + 1});
                max_value = max(max_value, value + 1);
            }
        }
    }
    return max_value;
}

int solution(int n, vector<vector<int>> edge)
{
    int answer = 0;

    for (auto ele : edge)
    {
        map[ele[0]].push_back(ele[1]);
        map[ele[1]].push_back(ele[0]);
    }

    int value = bfs();
    for (int i = 2; i <= n; i++)
    {
        if (dist[i] == value)
            answer += 1;
    }
    return answer;
}
