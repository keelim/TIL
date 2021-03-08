#include<algorithm>

using namespace std;

class Solution {
public:
    int getMaximumGenerated(int n) {
        if(n==0) return 0;
        if(n==1) return 1;
        int arr[201];

        arr[0] = 0;
        arr[1] = 1;
        
        for(int i=1; i<=n/2; i++){
            arr[2*i] = arr[i];
            arr[2*i+1] = arr[i]+arr[i+1];
        }

        return *max_element(arr, arr+n+1);
    }
};