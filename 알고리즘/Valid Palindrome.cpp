#include <string>

using namespace std;

class Solution {
public:
    char asciilower(char in){
        if('A'<=in&&in<='Z') return in - ('Z'-'z');
        else return in;
    }

    bool isPalindrome(string s) {
        int pointer1 = 0;
        int pointer2 = s.size()-1;
        char a =asciilower(s[pointer1]);
        char b=asciilower(s[pointer2]);
        while true{
            if(pointer1>=pointer2) return true;
            if(a==b){
                pointer1+=1;
                pointer2-=1;
                a = s[pointer1];
                while a==' '{
                    p
                }
                b = s[pointer2];
            }

        }
    }
};