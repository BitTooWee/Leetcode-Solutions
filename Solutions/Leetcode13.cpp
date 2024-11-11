class Solution {
public:
    int romanToInt(string s) {
        int Answer = 0;
        std::map<char,int> Values= { {'I',1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}};
        for (int i = 0; i<s.size();i++) {
            if (i < s.size() - 1) {
                if (Values.find(s[i])->second < Values.find(s[i + 1])->second) {
                    Answer += Values.find(s[i + 1])->second - Values.find(s[i])->second;
                    i++;
                } else {
                    Answer += Values.find(s[i])->second;
                }
            } else {
                Answer += Values.find(s[i])->second;
            }
        }
        return Answer;
    }
};
