import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    # Base case: if s is the empty string, return True.
    if len(s) == 0:
        return True

    # Recursive step: return True if the first and last characters of s are the same and
    # _isPalindrome(characters between first and last in s) is True; and False otherwise.
    if s[0] == s[len(s)-1]:
        return _isPalindrome(s[1:-1])
    else:
        return False


if __name__ == '__main__':
    main()
