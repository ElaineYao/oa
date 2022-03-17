## armaze & amazon
def resultWord(searchW, resultW):
    p1, p2 = 0, 0
    for i in range(len(searchW)):
        if searchW[p1] == resultW[p2]:
            p1 = p1+1
            p2 = p2+1
        else:
            p1 = p1+1
    return (p1-p2)

if __name__ == "__main__":
    s1 = "armaze"
    s2 = "amazon"
    print(resultWord(s1, s2))
    