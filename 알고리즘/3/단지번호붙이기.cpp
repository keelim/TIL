#include <bits/stdc++.h>

using namespace std;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int n;
int total_map[26][26];
bool visited[26][26];

vector<int> vc;

void bfs(int a, int b){
    queue<pair<int, int>> q;
    q.push(make_pair(a,b));
    visited[a][b]=1;
    int count=1;

    while (!q.empty()){
        int x, y;
        tie(x, y) = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];

            if(nx<0||ny<0||nx>=n||ny>=n) continue;
            
            if(total_map[nx][ny]==1&&!visited[nx][ny]){
                q.push(make_pair(nx, ny));
                visited[nx][ny]=1;
                count++;
            }
        }
    }

    vc.push_back(count);
}
int main() {
    cin>>n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%1d", &total_map[i][j]);
        }
    }
    int room=0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(visited[i][j]==0&&total_map[i][j]==1){
                room++;
                bfs(i, j);
            }
        }
    }

    sort(vc.begin(), vc.end());

    cout<<vc.size()<<'\n';
    for(auto ele: vc){
        cout<<ele<<'\n';
    }

    return 0;
}