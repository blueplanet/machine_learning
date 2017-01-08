# coding: utf-8

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDisIndicies = distances.argsort()

    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    file = open(filename)
    lines = file.readlines()
    count = len(lines)
    mat = zeros((count, 3))

    classLabelVector = []
    index = 0

    for line in lines:
        line = line.strip()
        columns = line.split(',')
        mat[index, :] = columns[0:3]
        classLabelVector.append(int(columns[-1]))
        index += 1

    return mat, classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    rows = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (rows, 1))
    normDataSet = normDataSet / tile(ranges, (rows, 1))

    return normDataSet, ranges, minVals

def show_plt():
    mat, labels = file2matrix('dat.csv')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mat[:, 1], mat[:, 2], 50.0 * array(labels), 100.0 * array(labels))
    plt.show()

def normMat():
    mat, labels = file2matrix('dat.csv')
    normMat, ranges, minVals = autoNorm(mat)
    print normMat

def datingClassTest():
    test_set_percent = 0.3
    errorCount = 0.0

    datingDataMat, datingLabels = file2matrix('test_set.csv')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    row_count = normMat.shape[0]
    training_count = int(row_count * test_set_percent)

    for i in range(training_count):
        classifierResult = classify0(normMat[i, :], normMat[training_count:row_count, :], \
            datingLabels[training_count:row_count], 3)

        print "the classifier came back with: %d, the real answer is: %d"\
            % (classifierResult, datingLabels[i])

        if (classifierResult != datingLabels[i]):
            errorCount += 1.0

    print "the total error rate is: %f" % (errorCount / float(training_count))

def classifyPerson():
    results = ['not at all', 'in small doses', 'in large doses']

    percentTats = float(raw_input('玩游戏的时间百分比'))
    ffMiles = float(raw_input('每年乘坐飞机的里程数'))
    iceCream = float(raw_input('每年冰淇淋的重量'))

    mat, labels = file2matrix('test_set.csv')
    normMat, ranges, minVals = autoNorm(mat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, labels, 3)

    print "你对这个人的喜爱程度：", results[classifierResult - 1]
