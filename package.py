def package(cmd):
    packs = []
    result = []
    if(cmd == [[]]):
        return -1
    for i in range(len(cmd)):
        # for each cmd
        if cmd[i][0] == "INSERT":
            packs.append(cmd[i][1])
        elif cmd[i][0] == "SHIP":
            if(len(packs)>2):
                result.append(packs[0:3])
                packs = []
            else:
                result.append(["N/A"])
        else:
            return -1
    return result


if __name__ == "__main__":
    cmds = [["INSERT", "UIAHSIHGFG"],["INSERT","RGSRTWR"],["SHIP","-"],["INSERT","EYJTRJYEYTJ"],["INSERT","QERGFSFDS"],["SHIP","-"]]
    print(package(cmds))
