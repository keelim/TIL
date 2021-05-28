class Solution {
public:
    int numberOfSteps (int num) {
        int i=0;
        while (num>0){
            i+=1;
            if(num&1){
                num-=1;
                continue;
            } else{
                num/=2;
                continue;
            }
        }
        return i;
    }
};