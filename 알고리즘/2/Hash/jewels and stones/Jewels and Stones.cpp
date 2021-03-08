class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        unordered_map<char, int> map;

        for (auto ele : stones)
        {
            map[ele] += 1;
        }

        int cnt = 0;
        for (auto ele : jewels)
        {
            cnt += map[ele];
        }

        return cnt;
    }
};