class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int closest = nums[0];
        for (int i = 1; i < nums.size();i++) {
            if (closest != NULL) {
                if (abs(nums[i]) < abs(closest)) {
                    closest = nums[i];
                } else {
                    if (abs(nums[i]) == abs(closest)) {
                        closest = std::max(nums[i],closest);
                    }
                }
            }
        }
        return closest;
    }
};