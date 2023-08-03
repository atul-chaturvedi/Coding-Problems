class Solution {
public:
    vector<string> numpad = {"", "", "abc", "def", "ghi", "jkl",
                                "mno", "pqrs", "tuv", "wxyz"};
    
    vector<string> ans;
    
    void help(string digits, int index, string curr){
        if(index == digits.size()){
            ans.push_back(curr);
            return;
        }
        for(char ch: numpad[digits[index] - '0']){
            help(digits, index+1, curr+ch);
        }
        
        
    }
    
    vector<string> letterCombinations(string digits) {
        if(digits.size() == 0)
            return {};
        help(digits, 0, "");  
        return ans;
    }
};