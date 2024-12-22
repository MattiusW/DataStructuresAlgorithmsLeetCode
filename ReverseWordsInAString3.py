def reverseWords(s: str) -> str:
    rev_string = ""

    for i in range(len(s)):
        cursor = i
        if s[i] == " " or i == len(s) - 1:
            while cursor >= 0 or s[cursor] != " ":
                if cursor == -1:
                    break
                rev_string += s[cursor]
                cursor -= 1

    return rev_string.strip()

def main():
    s = "Let's take"
    r = reverseWords(s)
    print(r)

if __name__ == "__main__":
    main()