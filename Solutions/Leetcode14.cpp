class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int min_length = strs[0].size();
        for (int i = 1; i < strs.size(); i++) {
            if (strs[i].size() < min_length) {
                min_length = strs[i].size();
            }
        }
        for (int i = 0; i < min_length; i++) {
            char current_prefix = strs[0][i];
            for (int j = 1; j < strs.size(); j++) {
                if (strs[j][i] != current_prefix) {
                    return strs[0].substr(0,i);
                }
            }
            if (i == min_length - 1) {
                return strs[0].substr(0,i+1);
            }
        }
        return "";
    }
};
