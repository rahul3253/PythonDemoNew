def comparator(tempdifference, tempDifferenceAllowed):
    if tempdifference <= tempDifferenceAllowed:
        return True


def tempdifference(temp, apiTemp):
    return abs(temp - apiTemp)

