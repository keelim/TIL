#include <string>

int solution(vector<int> people, int limit) {
    int answer = 0;
    int left = 0;
    int right = people.size() - 1;
    sort(people.begin(), people.end(), greater<>());  // 내림차순

    while (left <= right) { // 투포인터 알고리즘 왼쪽 오른쪽 탐색
        if (people[left] + people[right] <= limit)
            right--;
        left++;
        answer++;
    }

    return answer;
}

def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) -1
    people.sort(reverse = True)

    while left<=right:
        if people[left]+people[right] <=limit:
            right-=1
        left+=1
        answer+=1
        
    return answer