"""
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear 
in s have the same number of occurrences (i.e., the same frequency).
"""
from collections import defaultdict

def areOccurrencesEqual(s: str) -> bool:
    
    dic = defaultdict(int)
    unique = set()

    for i in s:
        dic[i] += 1    

    for value in dic:
        unique.add(dic[value])

    return False if len(unique) != 1 else True

def main():
    # Example 1:
    s1 = "abacbc"
    # Example 2:
    s2 = "aaabb"

    example1 = areOccurrencesEqual(s1)
    example2 = areOccurrencesEqual(s2)

    print(f"Example1: {example1}")
    print(f"Example2: {example2}")



if __name__ == "__main__":
    main()