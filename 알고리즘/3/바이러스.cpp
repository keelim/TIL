#include <bits/stdc++.h>
#include <queue>

using namespace std;

vector<int> map[101];
bool visited[101];
int cnt;

void bfs(int start){
    queue<int> q;
    q.push(start);
    visited[start] = 1
    int cnt = 0
    while(!q.empty()){
        int x = q.front();
        q.pop();

        for(auto ele : map[x]){
            if(!visited[ele]){
                q.push(ele);
                visited[ele]  = 1;
                cnt+=1;
            }
        }
    }
    cout<<cnt<<'\n';
}

void dfs(int start){
    visited[start] = 1;
    cnt+=1;

    for (auto ele: map[start]){
        if(!visited[ele]){
            dfs(ele);
        }
    }
}

int main(){
    int n;
    int t;
    cin>>n>>t;

    while(t--){
        int a, b;
        cin>>a>>b;
        map[a].push_back(b);
        map[b].push_back(a);
    }

    bfs(1);
    memset(visited, 0, sizeof(visited));

    dfs(1);
    cout<<cnt-1<<'\n';

    return 0;
}