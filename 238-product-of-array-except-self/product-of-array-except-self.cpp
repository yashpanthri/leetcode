class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n);
        int prefixProduct = 1;
        for (int i = 0; i<n; i++){
            answer[i] = prefixProduct;
            prefixProduct *= nums[i];
        }

        int postfixProduct = 1;
        for (int i = n-1; i>=0; --i){
            answer[i] *= postfixProduct;
            postfixProduct *= nums[i];
        }
        return answer;
    }
};