from collections import defaultdict


def check_for_hits(planets, counts):
    total = 0
    for planet in planets:
        if counts(planet):
            total += 1
    return total


def parse():
    for x in range(1, 8):
        file_name = "%02d" % x
        input_file = open(file_name + ".in")
        lines = input_file.read().splitlines()

        planets, ships = lines[0].split(" ")

        map_x = defaultdict(list)
        map_y = defaultdict(list)

        for i in range(1, int(planets) + 1):
            x, y = [int(k) for k in lines[i].split(" ")]
            map_x[x] += [y]
            map_y[y] += [x]

        start = int(planets) + 1
        hit_list = []
        for i in range(start, start + int(ships)):
            hits = 0
            x, y, direction = lines[i].split(" ")
            x, y = int(x), int(y)
            if direction == "U":
                hits += check_for_hits(map_x[x], lambda j: j > y)
            elif direction == "D":
                hits += check_for_hits(map_x[x], lambda j: j < y)
            elif direction == "L":
                hits += check_for_hits(map_y[y], lambda j: j < x)
            elif direction == "R":
                hits += check_for_hits(map_y[y], lambda j: j > x)
            else:
                raise "Invalid direction value %s" % direction
            hit_list.append(hits)

        output_file = open(file_name + ".out")
        should_be = [int(k) for k in output_file.readlines()]

        assert hit_list == should_be


if __name__ == '__main__':
    parse()
