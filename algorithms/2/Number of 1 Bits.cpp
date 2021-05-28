#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        string a = bitset<32> (n).to_string();
        int b = count(a.begin(), a.end(), '1');
        return b;
    }

    int hammingWeight2(uint32_t n) {
    int count = 0;
    
    while (n) {
        n &= (n - 1);
        // 뒤에서 부터 1을 지운다.
        count++;
    }
    
    return count;
}
};