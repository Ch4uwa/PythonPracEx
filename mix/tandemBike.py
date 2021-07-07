redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = False


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        redShirtSpeeds.sort(reverse=True)

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[i]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - i - 1]
        totalSpeed += max(rider1, rider2)

    return totalSpeed


print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
