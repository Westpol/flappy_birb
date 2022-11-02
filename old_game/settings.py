def loadSettings():
    global clockEnabled, frames_per_second, difficulty
    settings = open("settings.txt", "r")
    settingArray = settings.readlines()[0].split("$")
    settings.close()
    clockEnabled = bool(int(settingArray[0]))
    frames_per_second = int(settingArray[1])
    difficulty = int(settingArray[2])


def saveSettings():
    global frames_per_second, clockEnabled, difficulty
    settings = open("settings.txt", "r+")
    settings.truncate(0)
    settings.write(str(int(clockEnabled)))
    settings.write("$")
    settings.write(str(int(frames_per_second)))
    settings.write("$")
    settings.write(str(int(difficulty)))
    settings.close()
