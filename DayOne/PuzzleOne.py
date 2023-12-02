def calibrate(stupidElves):
    valueOne = -1
    valueTwo = -1
    for i in stupidElves:
        try:
            if valueOne < 0:
                valueOne = int(i)
                valueTwo = int(i)
            else:
                valueTwo = int(i)
        except:
            print()
    print(10 * valueOne + valueTwo)
calibrate("a7g")

