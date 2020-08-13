import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    dictionary = {}

    for char in str1:
        dictionary[char] = 0

    for char in str2:
        if char in dictionary:
            dictionary[char] += 1

    maxKey = ""
    maxValue = 0

    for key in dictionary:
        if dictionary[key] > maxValue:
            maxValue = dictionary[key]
            maxKey = key

    print(f"#{test_case} {maxValue}")