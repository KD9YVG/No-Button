database = "database.txt"
blockedData = "blocked.txt"
dataList = []
tempDataList = []
blockedPhrases = []

def importData(filter=True):
    with open(database, 'r', encoding='utf-8') as file:
        for line in file:
            tempDataList.append(line.strip())
    if filter:
        with open(blockedData, 'r', encoding='utf-8') as file:
            for line in file:
                blockedPhrases.append(line.strip())
        numBlocked = 0
        for x in range(len(tempDataList)):
            blocked = False
            for i in range(len(blockedPhrases)):
                if tempDataList[x] == blockedPhrases[i]:
                    blocked = True
                    numBlocked = numBlocked + 1
            if not blocked:
                dataList.append(tempDataList[x])    
    info = {
        "data": dataList,
        "dataPath": database,
        "blockedPath": blockedData,
        "amountBlocked": numBlocked
    }
    return info