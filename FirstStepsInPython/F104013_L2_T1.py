import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <comma-separated list> <string>")
    sys.exit(1)

isListSorted = [int(x) for x in sys.argv[1].split(',')]
isListSorted1 = list(sys.argv[2])

def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def isInAlphabeticalOrder(char):
    for i in range(len(char) - 1):
        if char[i] > char[i + 1]:
            return False
    return True

print(is_sorted(isListSorted))
print(isInAlphabeticalOrder(isListSorted1))