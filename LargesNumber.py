from collections import defaultdict

def largestUniqueNumber(nums):
    counts = defaultdict(int)
    check_list = []
        
    for i in nums:
        counts[i] += 1

    for value in counts:
        if counts[value] == 1:
            check_list.append(value)
     
    return max(check_list) if counts[value] == 1 else -1
            
print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))