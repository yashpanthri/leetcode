class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> mpp;

        for(auto it : nums){
            mpp[it] ++;
            if(mpp[it]>1){
                return true;
            }
        }
        return false;
    }
};