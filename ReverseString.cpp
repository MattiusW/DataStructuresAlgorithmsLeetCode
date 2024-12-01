#include <iostream>
#include <vector>

void reverseString(std::vector<char> &s)
{
    int left = 0;
    int right = s.size() - 1;

    while (left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }

    for (auto i : s)
        std::cout << i << " ";
}

int main(void)
{
    std::vector<char> s_origin = {'h', 'e', 'l', 'l', 'o'};
    char item;
    item = s_origin[2];
    std::cout << item << std::endl;

    for (auto i : s_origin)
        std::cout << i << " ";

    reverseString(s_origin);
}