def checkStraightLine(coordinates):
    k = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
    for p in range(2, len(coordinates)):
        if (coordinates[p][1]-coordinates[p-1][1])/(coordinates[p][0]-coordinates[p-1][0]) != k:
            print('false')
            sys.exit(0)

    print('true')
