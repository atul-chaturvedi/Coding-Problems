class Solution {
public:
    map<string, bool> mp;
    map<pair<int, string>, bool> dp;
    bool help(string s, int index, string curr_sub, int n){
        if(index >= n)
            return true;
        
        if(dp.find({index,curr_sub})!= dp.end())
                return dp[{index,curr_sub}];
            
        
        int j = index;
        string sub;
        bool ans = false;
        for(int i = index; i<n; i++){
            sub = s.substr(j, i - j+1);
            cout<<sub<<"\n";
            
            if(mp.find(sub) != mp.end()){
               bool temp  =  help(s, i+1, sub, n);
                dp[{i+1 ,sub}] = temp;
                // cout<<sub<<" "<<temp<<"\n";
                if(temp)
                    ans = true;
            }
            if(ans)
                break;
        }
        return ans;
    }

    bool wordBreak(string s, vector<string>& wordDict) {

        int n = s.size();
        for(auto word: wordDict){
            mp[word] = false;
        }
        
        
        return help(s,0,"", n);
    }

};