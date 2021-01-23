#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(auto ele : s) {
            if(stack.empty()) stack.push(ele);
            
            if(stack.top()=='['&& ele==']'){
                stack.pop();
                continue;
            }

            if(stack.top()=='('&& ele==')'){
                stack.pop();
                continue;
            }

            if(stack.top()=='{'&& ele=='}'){
                stack.pop();
                continue;
            }


        }
        return stack.empty()==0;
    }
};