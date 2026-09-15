class Solution {
public:
    vector<vector<int>> generate(int numRows) {

        vector<vector<int>> result;

        for( int i = 1 ; i < numRows+1; i= i+1){

            result.push_back(generateRow(i));
        }

        return result;        
        
    }

private:
    vector<int> generateRow(int row){
        vector<int> temp;
        long long ans = 1;
        temp.push_back(ans);

        for(int i = 1; i < row;i = i+1){

            ans = ans*(row-i);
            ans = ans/i;

            temp.push_back(ans);
        }

        return temp;
    }
};