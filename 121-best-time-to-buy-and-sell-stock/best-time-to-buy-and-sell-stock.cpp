class Solution {
public:
    int maxProfit(vector<int>& prices) {

    // //BRUTE FORCE
    //     int n = prices.size();
    //     int buy = -1;
    //     int sell = -1;
    //     int profit = 0;
    //     for(int i = 0; i<n-1; i++){
    //         for (int j = i+1; j<n-1; ++j){
    //             if((prices.at(j)-prices.at(i))>profit){
    //                 profit = prices.at(j)-prices.at(i);
    //                 buy = i;
    //                 sell = j;
    //             }
    //         }
    //     }
    //     return profit;
    // }

    int mini = prices[0];
    int maxProfit = 0;
    int n = prices.size();
    for (int i = 0; i < n ; ++i){
        int cost = prices[i] - mini;
        maxProfit = max(maxProfit, cost);
        mini = min(mini, prices[i]);
    }
    return maxProfit;
    }
};