#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> set;

        for (auto ele : nums)
        {
            if (set.empty())
            {
                set.insert(ele);
                continue;
            }
            auto it = set.find(ele);
            if (it == set.end())
            {
                set.insert(ele);
            }
            else
            {
                return true;
            }
        }

        return false;
    }

    bool containsDuplicate2(vector<int> &nums)
    {
        unordered_set<int> set(nums.begin(), nums.end());

        return (nums.size() != set.size()) ? true : false;
    }
};