class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int , int>hashmap;
        int n = nums.size();
        vector<int> result;

        for(int i = 0; i<n;i=i+1){

            hashmap[nums[i]]++;
        }

        for (auto& [key, value] : hashmap){

            if(hashmap[key] > n/3) result.push_back(key);
        }

        return result;

        
    }
};