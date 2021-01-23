class Solution {
public:
    void reverseString(vector<char>& s) {
        for(int i=0; i<s.size()/2; i++){
            int pointer = s.size()-1-i;
            swap(s[i], s[pointer]);
            // int temp = s[i];
            // s[i] = s[pointer];
            // s[pointer] = temp;
        }
    }
};