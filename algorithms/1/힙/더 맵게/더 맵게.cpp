#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;

    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());
    // min heap 으로 구현
    // 파이썬 max heap 이 미지원 이다.
    while (pq.top() < K && pq.size() > 1)
    {
        auto first = pq.top();
        pq.pop();
        // 엘리먼트 첫 번째 값을 꺼낸다

        auto second = pq.top() * 2;
        pq.pop();
        // 엘리먼트 두 번째 값을 꺼낸다.

        pq.push(first + second);
        answer += 1;
    }

    if (pq.top() < K)
        return -1;

    return answer;
}