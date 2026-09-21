class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {

        int n = arr.size();
        vector<int>result;
        vector<int> prefixxor(n);
        for(int i = 0; i<n;i++){

            if(i == 0){
                prefixxor[i] = arr[i];
            }
            else{
                prefixxor[i] = prefixxor[i-1]^arr[i];
            }
            
        }

        for(auto&query:queries){
            int l = query[0];
            int r = query[1];

            if(l == 0){
                result.push_back(prefixxor[r]);
            }
            else{
                result.push_back(prefixxor[r]^prefixxor[l-1]);

            }

        }

        return result;


        
    }
};