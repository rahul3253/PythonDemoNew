def comparator(tempdifference):
    if tempdifference <= 2:
        return True


def tempdifference(temp, apiTemp):
    return abs(temp - apiTemp)

