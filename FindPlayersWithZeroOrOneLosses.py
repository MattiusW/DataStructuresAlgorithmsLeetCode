"""
You are given an integer array matches 
where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
"""

from collections import defaultdict
from typing import List

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    anserw = [[],[]]
    dic_winners = defaultdict(int)
    dic_lossers = defaultdict(int)

    for winner, losser in matches:
        dic_winners[winner] += 1 
        dic_lossers[losser] += 1

    for winner in dic_winners:
        if winner not in dic_lossers:
            anserw[0].append(winner)

    for losser in dic_lossers:
        if dic_lossers[losser] == 1:
            anserw[1].append(losser)

    anserw[0].sort()
    anserw[1].sort()

    return anserw

def main():
    matches_one = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    matches_two = [[2,3],[1,3],[5,4],[6,4],]

    result1 = findWinners(matches=matches_one) 
    result2 = findWinners(matches=matches_two)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()