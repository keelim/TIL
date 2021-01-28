#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int index = haystack.find(needle);
        return index;
    }
};