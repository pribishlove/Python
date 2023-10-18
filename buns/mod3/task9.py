f = open("input.txt")
N = int(f.readline())
currentSteps = 1
x = 0
y = 0
currentCountSteps = 0
while N > 0:
    if currentCountSteps % 4 == 0:
        if (N >= currentSteps):
            x -= currentSteps
            N -= currentSteps
            currentCountSteps += 1
        else:
            x -= N
            break
    elif currentCountSteps % 4 == 1:
        if (N >= currentSteps):
            y -= currentSteps
            N -= currentSteps
            currentCountSteps += 1
        else:
            y -= N
            break
    elif currentCountSteps % 4 == 2:
        currentSteps += 1
        if (N >= currentSteps):
            x += currentSteps
            N -= currentSteps
            currentCountSteps += 1
        else:
            x += N
            break
    elif currentCountSteps % 4 == 3:
        if (N >= currentSteps):
            y += currentSteps
            N -= currentSteps
            currentSteps += 1
            currentCountSteps += 1
        else:
            y += N
            break
with open("output.txt", "a") as f:
    f.write(str(x) + " " + str(y))