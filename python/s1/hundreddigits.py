def getHundredDigits(a, b, c, d):
    threeNumberList = []
    fourNumberList = [a, b, c, d]

    for i in range(0, 4):
        if fourNumberList[i] == 0:
            continue
        HundredNumber = fourNumberList[i]
        for j in range(0, 4):
            if i == j:
                continue
            TenNumber = fourNumberList[j]
            for k in range(0, 4):
                if k == i or k == j:
                    continue
                SingleNumber = fourNumberList[k]

                ThreeNumber = HundredNumber*100+TenNumber*10+SingleNumber

                hasNumber = False
                for num in threeNumberList:
                    if ThreeNumber == num:
                        hasNumber = True

                if not hasNumber:
                    threeNumberList.append(ThreeNumber)

    return len(threeNumberList)
