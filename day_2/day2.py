import re

"Game 1: 1 green, 4 blue; 1 blue, 2 green, 1 red; 1 red, 1 green, 2 blue; 1 green, 1 red; 1 green; 1 green, 1 blue, 1 red"
with open("aoc2.txt", "r") as f:
    lines = f.readlines()
    possible_id_sum = 0

    for line in lines:
        possible = True
        game = line.split(":")
        game_id = int(re.findall("\d+", game[0])[0])
        
        showings = game[1].split(";")
        print(showings)
        break
        for show in showings:
            cubes = show.split(",")
            for cube in cubes:
                num = re.findall("\d+", cube)[0]
                if "red" in cube and int(num) > 12:
                    possible = False
                if "green" in cube and int(num) > 13:
                    possible = False
                if "blue" in cube and int(num) > 14:
                    possible = False
        if possible:
            possible_id_sum += game_id
            print(possible_id_sum)
    print(possible_id_sum)

