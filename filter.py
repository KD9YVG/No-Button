# This is a module imported by main.py, so all code needs to be run during import
# In other words, yes I know that this could have been writen more object-ey but
# this works perfectly fine for my uses.

database = "db/database.txt" # Database contents from hotheadhacker/no-as-a-service (https://github.com/hotheadhacker/no-as-a-service)
blockedData = "db/blocked.txt"
dataList = []
tempDataList = []
blockedPhrases = []

def importData(filter, debug):
    # Clears all lists and variable in case this function is called more than once
    numBlocked = 0
    dataList.clear()
    tempDataList.clear()
    blockedPhrases.clear()

    # Opens the database file and puts each line into the temporary data list
    with open(database, 'r', encoding='utf-8') as file:
        for line in file:
            tempDataList.append(line.strip())

    # If the function is called with the parameter filter set to true, it then loads all the blocked phrases and then
    # checks if any of the prases from the database match the blocked phrases
    if filter:
        with open(blockedData, 'r', encoding='utf-8') as file:
            for line in file:
                blockedPhrases.append(line.strip())

        for x in tempDataList: # We loop through every phrase
            blocked = False
            for i in blockedPhrases: # And compare it to every blocked phrase
                if debug: # If the function was called with the argument debug set to true, the program displays what phrases it is comparing to the terminal
                    print(tempDataList[x] + " \033[33equal to\033[0m " + blockedPhrases[i] + "\033[33m?\033[0m\x1b[34m " + str(tempDataList[x] == blockedPhrases[i]) + "\033[0m" )
                if tempDataList[x] == blockedPhrases[i]:
                    # If the phrase in the database and blocked list match, the blocked variable is set to true and the number of blocked phrases counter is incremented by 1
                    blocked = True
                    numBlocked += 1
            if not blocked: # If the blocked variable is not set to true (the phrase is not in the blocked list), the phrase is added to the final data list
                dataList.append(tempDataList[x])

    # All information about the filtering process, including statistics about how many prases were blocked and file paths is returned as a dictionary
    info = {
        "data": dataList,
        "dataPath": database,
        "blockedPath": blockedData,
        "amountBlocked": numBlocked
    }
    return info
