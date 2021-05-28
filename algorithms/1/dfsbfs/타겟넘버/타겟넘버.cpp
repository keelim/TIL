#include <bits/stdc++.h>

using namespace std;
vector<int> number;

int t;
int s=0;

void go (int index, int sum) {
    if (index == number.size ()) {
        if (sum == t) s+=1;
    }

    if (index >=number.size ()) return;

    go (index + 1, sum + number[index]);
    go (index + 1, sum - number[index]);
}

int solution (vector<int> numbers, int target) {
    number=numbers;
    t=target;

    go (0, 0);

    return s;
}

int main () {
    cout<<solution ({ 1, 1, 1, 1, 1 }, 3);
}