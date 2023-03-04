def largestFile():
    import sys
    max = 0
    for line in sys.stdin:
        line = line.split()
        if len(line) > 2:
            if int(line[4]) > max:
                max = int(line[4])
                name = line[8]
    print(name)
largestFile()