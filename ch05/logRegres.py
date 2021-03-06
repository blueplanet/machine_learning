from numpy import *

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

def plotBestFit(weights):
    import matplotlib.pyplot as plt

    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []; xcord2 = []; ycord2 = []

    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s = 30, c = 'red', marker = 's')
    ax.scatter(xcord2, ycord2, s = 30, c = 'green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

def stocGradAscent0(dataMat, classLabels):
    m, n = shape(dataMat)
    alpha = 0.01
    weights = ones(n)

    for i in range(m):
        h = sigmoid(sum(dataMat[i] * weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMat[i]

    return weights

def plotStoc():
    dataArr, labelMat = loadDataSet()
    weights = stocGradAscent0(array(dataArr), labelMat)
    plotBestFit(weights)

def stocGradAscent1(dataMat, classLabels, numlter = 150):
    m, n = shape(dataMat)
    weights = ones(n)

    for j in range(numlter):
        dataIndex = range(m)

        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMat[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMat[randIndex]
            del(dataIndex[randIndex])

    return weights


def plotStoc1():
    dataArr, labelMat = loadDataSet()
    weights = stocGradAscent1(array(dataArr), labelMat)
    plotBestFit(weights)

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5: return 1.0
    else: return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLables = []

    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        # TODO: lineArr = [float(value) for value in currLine[:21]]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLables.append(float(currLine[21]))

    trainWeights = stocGradAscent1(array(trainingSet), trainingLables, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print 'the error rate of this test is: %f' % errorRate
    return errorRate

def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print 'after %d iterations the aveage error rate is: %f' % (numTests, errorSum / float(numTests))
