class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pt1 = 0;
        int pt2 = numbers.size() - 1;

        while(true) {
            int sum = numbers[pt1] + numbers[pt2];
            if (sum == target) {
                return {pt1 + 1, pt2 + 1};
            }
            else if (sum > target) {
                pt2--;
            }
            else {
                pt1++;
            }
        }
    }
};
