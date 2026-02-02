name = input()
distinctLetters = set(name)
if len(distinctLetters)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")