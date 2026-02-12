database = "db/database.txt" # Database contents from hotheadhacker/no-as-a-service (https://github.com/hotheadhacker/no-as-a-service)
blockedData = "db/blocked.txt"
dataList = []
tempDataList = []
blockedPhrases = []

def importData(filter, debug):
    numBlocked = 0
    dataList.clear()
    tempDataList.clear()
    blockedPhrases.clear()
    with open(database, 'r', encoding='utf-8') as file:
        for line in file:
            tempDataList.append(line.strip())
    if filter:
        with open(blockedData, 'r', encoding='utf-8') as file:
            for line in file:
                blockedPhrases.append(line.strip())
        for x in range(len(tempDataList)):
            blocked = False
            for i in range(len(blockedPhrases)):
                if debug:
                    print(tempDataList[x] + " \033[33mequil to\033[0m " + blockedPhrases[i] + "\033[33m?\033[0m " + str(tempDataList[x] == blockedPhrases[i]))
                if tempDataList[x] == blockedPhrases[i]:
                    blocked = True
                    numBlocked += 1
            if not blocked:
                dataList.append(tempDataList[x])
    info = {
        "data": dataList,
        "dataPath": database,
        "blockedPath": blockedData,
        "amountBlocked": numBlocked
    }
    return info