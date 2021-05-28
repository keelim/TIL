#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int uniqueMorseRepresentations(vector<string> &words)
    {
        string morse[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        string alpha = "abcdefghijklmnopqrstuvwxyz";

        unordered_map<char, string> map;

        for (int i = 0; i < 26; i++)
        {
            map[alpha[i]] = morse[i];
        }
        set<string> set1;
        for (auto ele : words)
        {
            string result = "";
            for (auto ele1 : ele)
            {
                result+=map[ele1];
            }
            set1.insert(result);
        }
        return set1.size();
    }
};