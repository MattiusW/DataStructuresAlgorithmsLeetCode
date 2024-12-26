from collections import defaultdict
from typing import List

def canConstruct(ransomNote: str, magazine: str) -> bool:

    ransom_dic = defaultdict(int)
    magazine_dic = defaultdict(int)

    for i in ransomNote:
        ransom_dic[i] += 1

    for j in magazine:
         magazine_dic[j] += 1

    for key in ransom_dic:
        if key not in magazine_dic or ransom_dic[key] > magazine_dic[key]:
                return False

    return True

def main():
    example1 = canConstruct(ransomNote = "a", magazine = "b")
    example2 = canConstruct(ransomNote = "aa", magazine = "ab")
    example3 = canConstruct(ransomNote = "aa", magazine = "aab")
    example = canConstruct(ransomNote = "bg", magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
    exampleX = canConstruct(ransomNote = "fihjjjjei", magazine = "hjibagacbhadfaefdjaeaebgi")

    print(example1)
    print(example2)
    print(example3)
    print(example)
    print(exampleX)

if __name__ == "__main__":
    main()