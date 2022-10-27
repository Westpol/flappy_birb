import random
import math


def generateWorld(mapWidth, mapHeight):
    ps = 70      # probability straight
    psw = 40    # probability sidewinder
    pde = 4     # probabiltiy dead end
    pt = 12     # probability turn
    pcr = 30     # probability crossing
    world = [0]*(mapWidth*mapHeight)
    entryPoint = random.randint(1, mapWidth-1)
    exitPoint = random.randint(1, mapWidth-1)
    world[entryPoint] = 2
    world[(mapWidth * mapHeight) - exitPoint] = 3
    turning = [(entryPoint + mapWidth, 3)]   # 1 = up, 2 = left, 3 = down, 4 = right
    world[turning[0][0]] = 1
    turning[0] = (turning[0][0], turning[0][1] + 1)
    while 1:
        if len(turning) == 0:
            if checkValidity(world, mapWidth):
                return world
            else:
                return -1
        for i in range(len(turning)):
            whatwillhappen = random.randint(1, ps + psw + pde + pt)
            if 0 < whatwillhappen < ps: # straight lol
                if moveTo(turning[i][0], turning[i][1], mapWidth, mapHeight, world) != -1:
                    turning[i] = moveTo(turning[i][0], turning[i][1], mapWidth, mapHeight, world)
                    world[turning[i][0]] = 1
                else:
                    turning.pop(i)
                    break
            elif ps < whatwillhappen < ps + psw: # sidewinder
                if random.randint(0, 1) == 0:
                    turning.append((turning[i][0], turning[i][1] + 1))
                else:
                    turning.append((turning[i][0], turning[i][1] - 1))
                moveTo(turning[-1][0], turning[-1][1], mapWidth, mapHeight, world)
                break
            elif ps + psw < whatwillhappen < ps + psw + pde: # dead end
                turning.pop(i)
                break
            elif ps + psw + pde < whatwillhappen < ps + psw + pde + pt: # turn
                if random.randint(0, 1) == 0:
                    turning[i] = (turning[i][0], turning[i][1]+1)
                else:
                    turning[i] = (turning[i][0], turning[i][1]-1)
            elif ps + psw + pde + pt < whatwillhappen < ps + psw + pde + pt + pcr:  # sidewinder
                turning.append((turning[i][0], turning[i][1] + 1))
                turning.append((turning[i][0], turning[i][1] - 1))
                if moveTo(turning[len(turning)-2][0], turning[len(turning)-2][1], mapWidth, mapHeight, world) != -1:
                    turning[len(turning)-2] = moveTo(turning[len(turning)-2][0], turning[len(turning)-2][1], mapWidth, mapHeight, world)
                    world[turning[len(turning)-2][0]] = 1
                else:
                    turning.pop(len(turning)-2)
                if moveTo(turning[-1][0], turning[-1][1], mapWidth, mapHeight, world) != -1:
                    turning[-1] = moveTo(turning[-1][0], turning[-1][1], mapWidth, mapHeight, world)
                    world[turning[-1][0]] = 1
                else:
                    turning.pop(-1)
                break


def checkValidity(inpu, mw):
    if inpu.count(1) >= 1900 and inpu[inpu.index(3)-mw] == 1:
        return True
    return False


def moveTo(index, direction, microWave, microHeight, wd):
    newIndex = 0
    if direction == 1:
        newIndex = index - microWave
    if direction == 2:
        newIndex = index - 1
    if direction == 3:
        newIndex = index + microWave
    if direction == 4:
        newIndex = index + 1
    if not (math.floor(newIndex / microWave) == math.floor((newIndex + 1) / microWave)) or not (
            math.floor(newIndex / microWave) == math.floor((newIndex - 1) / microWave)):        # walls
        return -1
    if not (microWave < newIndex < (microWave * microHeight) - microWave):      # upper/lower limits
        return -1
    if wd[newIndex] == 1:       # passing into existing hall
        return -1
    if direction == 1:
        if wd[newIndex+1] == 1 and wd[newIndex+1+microWave] == 1 or wd[newIndex-1] == 1 and wd[newIndex-1-microWave] == 1:    # check for paralel
            return -1
    if direction == 2:
        if wd[newIndex-microWave] == 1 and wd[newIndex-microWave+1] == 1 or wd[newIndex+microWave] == 1 and wd[newIndex+microWave+1] == 1:    # check for paralel
            return -1
    if direction == 3:
        if wd[newIndex+1] == 1 and wd[newIndex+1-microWave] == 1 or wd[newIndex-1] == 1 and wd[newIndex-1-microWave] == 1:    # check for paralel
            return -1
    if direction == 4:
        if wd[newIndex-microWave] == 1 and wd[newIndex-microWave-1] == 1 or wd[newIndex+microWave] == 1 and wd[newIndex+microWave-1] == 1:    # check for paralel
            return -1
    return newIndex, direction
