#!/usr/bin/env python
import sys
import collections
import argparse


#usage: python CommonLongestString.py --string1 abedexyz --string2 xyzabede --mismatch 1

__author__ = "Zhikun Wu"
__date__ = "2018.11.13"
__email__ = "598466208@qq.com"

def hamming_distance(string1, string2):
    """
    Hamming distance for two string
    """
    count = 0
    if len(string1) == len(string2):
        for i in range(len(string1)):
            s1 = string1[i]
            s2 = string2[i]
            if s1 == s2:
                count += 1
        return count
    else:
        print("Please check whether the lengths of two strings are identical.")
        sys.exit(1)


def string_sliding(string1, string2, mismatch, NumberStrings):
    """
    One string as anchor, another string sliding with one character
    """
    strLen1 = len(string1)
    strLen2 = len(string2)
    for l in range(strLen1):
        str1 = string1[l:]
        for j in range(strLen2):
            str2 = string2[j:]
            minLen = min([len(str1), len(str2)])
            newStr1 = string1[l:l+minLen]
            newStr2 = string2[j:j+minLen]
            # print(newStr1)
            # print(newStr2)
            hammingDistance = hamming_distance(newStr1, newStr2)
            # if (minLen - hammingDistance) <= mismatch:
            NumberStrings[hammingDistance].append([newStr1, newStr2])

def longest_common_substring(string1, string2, mismatch):
    NumberStrings = collections.defaultdict(list)
    mismatch = int(mismatch)
    ### one string as anchor, another string sliding with one character
    string_sliding(string1, string2, mismatch, NumberStrings)
    string_sliding(string2, string1, mismatch, NumberStrings)
    ### deal with the result dict
    sortedKeys = sorted(list(NumberStrings.keys()), reverse=True)
    longest = sortedKeys[0]
    strings = NumberStrings[longest]
    for i in range(len(strings)):
        substr1 = strings[i][0]
        substr2 = strings[i][1]
        if substr1 in string1 and substr2 in string2:
            print("\nThe longest common substrings of '%s' and '%s' are '%s' and '%s' with up to %s mismatch.\n" % (string1, string2, substr1, substr2, mismatch))
        else:
            print("\nThe longest common substrings of '%s' and '%s' are '%s' and '%s' with up to %s mismatch.\n" % (string2, string1, substr1, substr2, mismatch))


def main():
    parser = argparse.ArgumentParser(description="Get the longest common substring with k mismatch for two strings.")
    parser.add_argument("-s1", "--string1", help="The input string one.")
    parser.add_argument("-s2", "--string2", help="The input string two.")
    parser.add_argument("-m", "--mismatch", help="The mismatch number of two strings.")
    args = parser.parse_args()
    longest_common_substring(args.string1, args.string2, args.mismatch)

if __name__ == "__main__":
    main()


