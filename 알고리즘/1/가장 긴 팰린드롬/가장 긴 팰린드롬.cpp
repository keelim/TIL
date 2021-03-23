#include <bits/stdc++.h>

using namespace std;

bool palindrome(string s, int length)
{
    for (int i = 0; i < s.size() - length + 1; i++)
    {
        string temp_a(s.begin() + i, s.begin() + i + length);
        string temp_b = temp_a;
        reverse(temp_b.begin(), temp_b.end());
        if (temp_a == temp_b)
        {
            return true;
        }
    }
    return false;
}

int solution(string s)
{
    string rs = s;
    reverse(rs.begin(), rs.end());
    int n = s.size();
    if (s == rs)
    {
        return s.size();
    }
    else
    {
        for (int i = n; i >= 2; i--)
        {
            if (palindrome(s, i))
                return i;
        }

        return 1;
    }
}