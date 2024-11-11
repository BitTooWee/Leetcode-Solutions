int Rec_Substrings(std::map<std::string,int> prev_substrings, std::string rest_string) {
    int max = -1;
    if (rest_string == "") {
        return 0;
    }

    for (int i = 0; i < rest_string.size(); i++) {
        if (prev_substrings.find( rest_string.substr(0,i+1) ) == prev_substrings.end() ) {

            std::map<std::string,int> prev = prev_substrings;
            prev.insert({rest_string.substr(0,i+1) , 0});
            std::string rest = "";
            if (rest_string.size() > 1) {
                    rest = rest_string.substr(i+1,rest_string.size()-i-1);
            }

            int l = Rec_Substrings(prev,rest);
            if (l > max) {
                max = l;
            }
        }
    }
    return max + 1;
}

class Solution {
public:
    int maxUniqueSplit(string s) {
        std::map<std::string,int> Answer = {};
        
        return Rec_Substrings(Answer, s);
    }
};
