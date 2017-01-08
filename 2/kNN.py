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

def show_plt():
    mat, labels = file2matrix('dat.csv')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mat[:, 1], mat[:, 2], 50.0 * array(labels), 100.0 * array(labels))
    plt.show()
