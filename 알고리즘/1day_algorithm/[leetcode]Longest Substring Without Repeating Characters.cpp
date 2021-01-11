#include <string>
#include <unordered_set>
using namespace std;

class Solution{
public:
    int lengthOfLongestSubstring(string s){
        unordered_set<char> set;

        int left = 0;
        int right = 0;
        int length = s.size();
        int answer = 0;

        while (left < length && right < length){
            if (set.find(s[right]) == set.end()){ //못찾으면
                set.insert(s[right]);             //셋에 넣고
                right++;                          //포인터를 넣고
                answer = max(answer, right - left); 
            } else{
                set.erase(s[left]); //있으면 셋에서 지우고
                left++;             //left pointer 를 증가시킨다
            }
        }
        return answer;
    }
};