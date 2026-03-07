t = int(input())
for _ in range(t):
    n = int(input())
    skills = list(map(int,input().split()))
    #2 8 6 3 1
    skills.sort()
    i = 0
    j = n-1
    isPos = False
    #1 2 3 6 8
    elite = []
    crowd = []
    while i < j:
        if skills[j] > skills[i]:
            if skills[j] not in elite:
                elite.append(skills[j])
            if skills[i] not in crowd:
                crowd.append(skills[i])
            i += 1
            print(elite)
            print(crowd)
        if len(elite) < len(crowd) and sum(elite) > sum(crowd):
            isPos = True
            break

    if isPos:
        print("YES")
    else:
        print("NO")



            