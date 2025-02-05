class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        //FTS By Me, POTD
        int n=s1.size();
        int check=0;
        int fd=0,sd=0;
        for(int i=0;i<n;i++){
            if(s1[i]!=s2[i]){
                check++;
                if(check>2)return false;
                else if(check==1)fd=i;
                else sd=i;
            }
        }
        return s1[fd]==s2[sd] && s1[sd]==s2[fd];
    }
};