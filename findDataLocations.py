def findDataLocations(locations, movedFrom, movedTo):
    for i in range(len(movedFrom)):
        locations.remove(movedFrom[i])
        locations.append(movedTo[i])
    locations.sort()
    return locations

if __name__ == "__main__":
    locations = [1, 7, 6, 8]
    movedFrom = [1, 7, 2]
    movedTo = [2, 9, 5]
    print(findDataLocations(locations, movedFrom, movedTo))

