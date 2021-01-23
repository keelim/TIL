#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;


    for(int i=0; i<numbers.size(); i++){
        for (int j = i+1; j < numbers.size(); ++j) {
                answer.push_back(numbers[i]+numbers[j]);
        }
    }
    unordered_set s  = unordered_set(answer.begin(), answer.end());
    answer = vector(s.begin(), s.end());
    sort(answer.begin(), answer.end());

    return answer;
}