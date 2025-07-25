class Solution {
    unordered_map< string, int> mpp;
    vector<vector<string>> ans;
    string b;

public:
    void dfs(string word, vector<string> &seq){
        if(word == b){
            reverse(seq.begin(), seq.end());
            ans.push_back(seq);
            reverse(seq.begin(), seq.end());
            return;
        }

        int steps = mpp[word];
        int n = word.size();
        for(int i = 0; i < n; i++){
            char og = word[i];
            for(char ch = 'a'; ch <= 'z'; ch++){
                word[i] = ch;
                if(mpp.find(word) != mpp.end() && mpp[word] == steps - 1){
                    seq.push_back(word);
                    dfs(word, seq);
                    seq.pop_back();
                }
            }
            word[i] = og;
        }
    }
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        queue<string> q;
        unordered_set<string> st(wordList.begin(), wordList.end());
        b = beginWord;
        q.push(beginWord);
        mpp[beginWord] = 1;
        st.erase(beginWord);
        int n = beginWord.size();
        while(!q.empty()){
            string word = q.front();
            int steps = mpp[word];
            q.pop();

            for(int i = 0; i < n; i++){
                char og = word[i];
                for(int ch  = 'a'; ch <= 'z'; ch++){
                    word[i] = ch;
                    if(st.find(word) != st.end()){
                        st.erase(word);
                        q.push(word);
                        mpp[word] = steps + 1;
                    }
                }
                word[i] = og;
            }
            if( word == endWord) break;
        }

        if(mpp.find(endWord) != mpp.end()){
            vector<string> seq;
            seq.push_back(endWord);
            dfs(endWord, seq);
        }

        return ans;
    }
};