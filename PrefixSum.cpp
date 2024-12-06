#include <iostream>
#include <vector>

std::vector<int> runningSum(std::vector<int> &nums)
{
    std::vector<int> prefix = {nums[0]};

    for (int i = 1; i < nums.size(); i++)
    {
        prefix.push_back(nums[i] + prefix[prefix.size() - 1]);
        std::cout << prefix[i] << std::endl;
    }

    return prefix;
}

int main(void)
{
    std::vector<int> nums1 = {1, 2, 3, 4};
    std::vector<int> nums2 = {1, 1, 1, 1, 1};

    for (auto i : nums1)
    {
        std::cout << i << " ";
    }

    std::cout << std::endl;

    for (auto j : nums2)
        std::cout << j << " ";

    std::cout << std::endl;

    std::vector<int> ans1 = runningSum(nums1);

    for (auto k : ans1)
    {
        std::cout << k << " ";
    }

    return 0;
}