class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {

        set<pair<int , int>> st;
        int n = matrix.size();
        
        //Transporse
        for(int i = 0; i<n ; i++){
            for(int j = 0; j<n ; j++){

                if (!(st.find({j,i}) != st.end())){

                    swap(matrix[i][j] , matrix[j][i]);   
                }
                st.insert({j,i});
                st.insert({i,j});
            }
        }

        // reverse row

        for(int i = 0; i<n; i++){

            int limit = n-1;
            limit = limit/2;

            for(int j = 0; j<=limit ; j++){

                swap(matrix[i][j] , matrix[i][n-1-j]);
            }
        }





        
    }
};