def grey(pixels):
    greyness = 0
    selfVal = 0
    if pixels==[[]]:
        return -1
    rows = len(pixels)
    cols = len(pixels[0])
    row_1s = [sum(i) for i in pixels]
    col_1s = [sum(j) for j in zip(*pixels)]
    print(row_1s)
    print(col_1s)
    for i in range(rows):
        for j in range(cols):
            if (pixels[i][j] == 0):
                temp = 2*(row_1s[i]+col_1s[j]) - (rows+cols)+1
            else:
                temp = 2*(row_1s[i]+col_1s[j]) - (rows+cols)- 1
            if temp>greyness:
                greyness = temp
                print("i = "+ str(i) +", j = "+str(j)+", grey = "+str(greyness))
    return greyness

if __name__ == "__main__":
    pixels = [
        [0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1]
    ]
    print(grey(pixels))