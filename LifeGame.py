import random, time

size: int = 25


def printlf(lifemap):
    for x in range(size):
        for y in range(size):
            if y == size - 1:
                print(lifemap[x][y])
            else:
                print(lifemap[x][y], end=" ")


def check(lifemap):
    n = 0
    point = [0 for i in range(size*size)]
    for x in range(size):
        for y in range(size):
            life = 0
            for xplus in range(-1, 2):
                for yplus in range(-1, 2):
                    if (xplus == 0) and (yplus == 0):
                        continue
                    if (x + xplus >= 0) and (x + xplus < size) and (y + yplus >= 0) and (y + yplus < size) and (
                            lifemap[x + xplus][y + yplus] == "●"):
                        life += 1
            if lifemap[x][y] == "●":
                if (life == 1) or (life == 0):
                    point[n] = 1
                elif (life == 2) and (life == 3):
                    point[n] = 2
                elif life >= 4:
                    point[n] = 1
            else:
                    if life == 3:
                        point[n] = 3
            n += 1
    return point


def getnext(lifemap, point):
    n = 0
    for x in range(size):
        for y in range(size):
            if point[n] == 1:
                lifemap[x][y] = "○"
            if point[n] == 3:
                lifemap[x][y] = "●"
            n += 1
    return lifemap


if __name__ == '__main__':
    lifeMap = [[0 for i in range(size)] for j in range(size)]
    for x in range(size):
        for y in range(size):
            dl = random.randint(0, 1)
            if dl == 0:
                lifeMap[x][y] = "○"
            else:
                lifeMap[x][y] = "●"
    print("初始状态为：")
    printlf(lifeMap)
    print("==========")

    n = 0
    num = 0
    while True:
        point = check(lifeMap)
        lifeMap = getnext(lifeMap, point).copy()
        num += 1
        print("第{0}次变化：".format(num))
        printlf(lifeMap)
        print("===========")
        # n = int(input("输入0继续进行下一步，输入其他数字退出。"))
        time.sleep(0.2)
