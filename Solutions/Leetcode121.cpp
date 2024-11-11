class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int current_count = 0;
        for (int i = 1; i < prices.size(); i++) {
            current_count += prices[i] - prices[i-1];
            if (current_count < 0) {
                current_count = 0;
            }
            if (current_count > max) {
                max = current_count;
            }
        }
        if (max > 0) {
            return max;
        } else {
            return 0;
        }
    }
};
