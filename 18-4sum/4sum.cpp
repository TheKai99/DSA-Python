class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {

        int n = nums.size();
        sort(nums.begin() , nums.end());
        vector<vector<int>> ans;

        for (int i = 0; i<n ; i++){

            if(i>0 && nums[i] == nums[i-1])continue;
            for(int j = i+1; j < n; j++){

                if(j>i+1 && nums[j] == nums[j-1])continue;

                int k = j+1;
                int l = n-1;

                while(l > k){
                    long long sum = nums[i] + nums[j];
                    sum+= nums[k] + nums[l];

                    if(sum > target){
                        l--;
                    }
                    else if(sum < target){
                        k++;
                    }
                    else{
                        vector<int> temp = {nums[i] , nums[j] , nums[k] ,nums[l]};
                        ans.push_back(temp);
                        k++;
                        l--;

                        while(l > k && nums[k] == nums[k-1]) k++;
                        while(l > k && nums[l] == nums[l+1]) l--;

                    }
                }
            }

                

            
        }
        return ans;


        
    }
};