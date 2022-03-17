
def findMinHealth(power, armor):
    return sum(power)-min(armor, max(power))+1

if __name__ == "__main__":
    p1 = [1, 2, 6, 7]
    p2 = 5
    print(findMinHealth(p1, p2))