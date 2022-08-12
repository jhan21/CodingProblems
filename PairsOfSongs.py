def numPairsDivisibleBy60(times):
    counter = [0] * 60
    total = 0

    for time in times:
        target = (60 - (time % 60)) % 60
        total += counter[target]
        counter[time % 60] += 1
    return total

time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))

