class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        //Using BFS algorithn to find the all the possible words and then finding them into the
        //set and then moving on if the word at any moment equals the endWord we found it and return 
        //the steps else we return 0
        //TC - O(n * word.size() * 26 * logn) SC - O(2n)
        queue<pair<string, int>> q;
        unordered_set<string> st(wordList.begin(), wordList.end());
        q.push({beginWord, 1});
        st.erase(beginWord);
        while( !q.empty()){                             //O( n == len(wordList))
            string word = q.front().first;
            int steps = q.front().second;
            q.pop();

            for(int i = 0; i < word.size(); i++){       //O(word.size())
                int original = word[i];
                for(char j = 'a'; j <= 'z'; j++){       //O(26)
                    word[i] = j;
                    if(st.find(word) != st.end()){      //O(logn)
                        st.erase(word);
                        q.push({word, steps + 1});
                    }
                }
                word[i] = original;
            }
            if(word == endWord){
                return steps;
            }
        }
        return 0;
    }
};