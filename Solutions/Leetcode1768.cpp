class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string result = "";
        int length = 0;
        for (int i = 0; i < word1.size() && i < word2.size();i++) {
            result += word1[i];
            result += word2[i];
            length += 1;
        }
        if (word1.size() > word2.size()) {
            result += word1.substr(length);
        } else if (word1.size() < word2.size()){
            result += word2.substr(length);
        }
        return result;
    }
};
