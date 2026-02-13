def longestCommonPrefix(strs):
    prefix = strs[0]
    print(prefix)
    for i in range(1, len(strs)):
        print(strs[i])
        while not strs[i].startswith(prefix):
            prefix = prefix[:len(prefix)-2]
            print(prefix)
    if prefix == "":
        return "no match"
    else:
        return prefix
print(longestCommonPrefix(["ab", "a"]))