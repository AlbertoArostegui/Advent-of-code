import re

with open("aoc2.txt", "r") as f:
    lines = f.readlines()
    
    power = 0
    for line in lines:
        red = 0
        green = 0
        blue = 0
        game = line.split(":")
        game_id = int(re.findall("\d+", game[0])[0])
        num = 0

        showings = game[1].split(";")
        for show in showings:
            cubes = show.split(",")
            for cube in cubes:
                num = int(re.findall("\d+", cube)[0])
                if "red" in cube:
                    if num > red:
                        red = num
                if "green" in cube:
                    if num > green:
                        green = num
                if "blue" in cube:
                    if num > blue:
                        blue = num
        num = red * green * blue
        power += num
    print(power)
