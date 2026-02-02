import string
n = int(input())
wordInput = input()

def checkPanagram(wordInput):
    word = wordInput.lower()
    lower = string.ascii_lowercase

    for char in lower:
        if char not in word:
            return "NO"
    return "YES"
    
print(checkPanagram(wordInput))


