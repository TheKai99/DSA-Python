class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        int n = nums.size();
        int sum = 0;
        int count = 0;

        for( int i = 0; i <n; i = i+1){

            sum = 0;

            for( int j = i ; j < n; j = j+1 ){

                sum = sum + nums[j];

                if ( sum == k) count = count + 1;
            }


        }

        return count;

    }

        
};