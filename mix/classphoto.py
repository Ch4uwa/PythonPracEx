redHeights = [5, 8, 1, 3, 4]
blueHeights = [6, 9, 2, 4, 5]


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    first_row = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    for i in range(len(redShirtHeights)):
        if first_row == 'RED':
            if redShirtHeights[i] > blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] > redShirtHeights[i]:
                return False

    return True


print(classPhotos(redHeights, blueHeights))
