#include <iostream>
#include <vector>

std::vector<int> sortedSquares(std::vector<int> &nums)
{
    std::vector<int> ans = {};

    int left = 0;
    int right = nums.size() - 1;

    // for (int i = 0; i < nums.size(); i++)
    // {
    //     if (abs(nums[left]) > abs(nums[right]))
    //     {
    //         ans.push_back(nums[left] * nums[left]);
    //         left++;
    //     }
    //     else
    //     {
    //         ans.push_back(nums[right] * nums[right]);
    //         right--;
    //     }
    // }

    for (auto i = nums.begin(); i < nums.end(); i++)
    {
        if (abs(nums[left]) > abs(nums[right]))
        {
            ans.insert(ans.begin(), (nums[left] * nums[left]));
            left++;
        }
        else
        {
            ans.insert(ans.begin(), (nums[right] * nums[right]));
            right--;
        }
    }

    return ans;
}

int main(void)
{
    // std::vector<int> origin_nums = {-7, -3, 2, 3, 11};
    std::vector<int> origin_nums = {-5, -3, -2, -1};

    std::cout << "Orginal table: ";

    for (auto i : origin_nums)
        std::cout << i << " ";

    std::cout << std::endl;

    std::vector<int> sorted_squeres_vector = sortedSquares(origin_nums);

    std::cout << "Sorted and squares vector: ";

    for (auto j : sorted_squeres_vector)
        std::cout << j << " ";

    std::cout << std::endl;
}