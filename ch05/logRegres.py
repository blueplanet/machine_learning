def loadDataSet():
    dataMat = []
    labelMat = []

    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append((1.0, float(lineArr[0]), float(lineArr[1])))
        labelMat.append(int(lineArr[2]))

    return dataMat, labelMat

def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

def gradAscent(dataMat, classLabels):
    dataMat = mat(dataMat)
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMat)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMat * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMat.transpose() * error

    return weights
