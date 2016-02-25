for x in range(1, 26):
    file_name = "%02d" % x
    input_file = open(file_name + ".in")
    lines = input_file.read().splitlines()

    found = False
    squadron_numbers = lines[1].split(" ")
    parsed_numbers = {}
    for amount in squadron_numbers:
        if amount in parsed_numbers:
            found = True
            break

        parsed_numbers[amount] = 1

    output_file = open(file_name + ".out")
    should_be = output_file.readlines()[0] == "YES"

    print("%s calculated %s and should be %s" % (x, found, should_be))
    assert found == should_be
