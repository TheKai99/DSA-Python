class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin() , nums.end());

        vector<vector<int>> ans;
        int n = nums.size();

        for(int left = 0; left < n; left++){

            if( left > 0 && nums[left] == nums[left-1]) continue;

            int middle = left + 1;
            int right = n-1;

            while ( middle < right){

                int sum = nums[left] + nums[middle] + nums[right];

                if(sum < 0 ){
                    middle++;

                }

                else if(sum > 0){
                    right--;
                
                }

                else {

                    vector<int> temp = {nums[left] , nums[middle] , nums [right]};
                    ans.push_back(temp);
                    middle++;
                    right--;
                    while(right > middle && nums[middle] == nums[middle-1]) middle++;
                    while(right > middle && nums[right] == nums[right+1]) right--;

                }

            }
        }
        return ans;
        
    }
};