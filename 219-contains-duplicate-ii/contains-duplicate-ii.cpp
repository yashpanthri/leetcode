class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
     std::unordered_map<int, int> mpp;
     for(auto i = 0; i<nums.size(); ++i){
        // if(mpp.find(nums[i])!=mpp.end()){
        //     if(abs(i-mpp[nums[i]])<=k){
        //         return true;
        //     }
       if(mpp.count(nums[i])){
            if(i-mpp[nums[i]]<=k){
                return true;
            }
        }
        mpp[nums[i]] = i;

     }  
     return false;

    }
};