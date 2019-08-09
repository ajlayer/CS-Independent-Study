#K Nearest Neighbors for CS360 Final Project 

count = 0
import csv
import random
import math
import operator
import sys

print("Training Set, Test Set, Accuracy(%), Counts")

# Read in dataset 
def loadDataset(filename, split, trainingSet=[], testSet=[]):

    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        global count
        count += 1
        dataset = list(lines)
        count += 1
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = (dataset[x][y])
                count += 1
            if random.random() < split:
                trainingSet.append(dataset[x])
                count += 1
            else:
                testSet.append(dataset[x])
                count += 1
        count += 1
    count += 1

# Calculate Euclidean distance 
def euclideanDistance(instance1, instance2, length):
    global count
    distance = 0
    count += 1
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
        count += 1
    return math.sqrt(distance)
count += 1

# Get the K nearest Neighbors 
def getNeighbors(trainingSet, testInstance, k):
    global count
    distances = []
    count += 1
    length = len(testInstance) - 1
    count += 1
    for x in range(len(trainingSet)):
        #print(x)
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        count += 1
        distances.append((trainingSet[x], dist))
        count += 1
    distances.sort(key=operator.itemgetter(1))
    count += 1
    neighbors = []
    count += 1
    for x in range(k):
        neighbors.append(distances[x][0])
        count += 1
    return neighbors
count += 1

# Determine the type of the unknown value based on its neighbors 
def getResponse(neighbors):
    global count
    classVotes = {}
    count += 1
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        count += 1
	#print(response)
        if response in classVotes:
            classVotes[response] += 1
            count += 1
        else:
            classVotes[response] = 1
            count += 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    count += 1
    return sortedVotes[0][0]
count += 1

# Calculate the accuracy of the model 
def getAccuracy(testSet, predictions):
    global count
    correct = 0
    count += 1
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            count += 1
            correct += 1
            count += 1
    return (correct / float(len(testSet))) * 100.0
count += 1

# Main 
def main(fileName):
    # prepare data
    global count
    trainingSet = []
    trainingSet2 = []
    trainingSet3 = []
    count += 1
    testSet = []
    testSet2 = []
    testSet3 = []
    count += 1
    split = 0.67
    count += 1
    #loadDataset(fileName, split, trainingSet, testSet)
    count += 1

    with open('test_set.csv', 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in dataset:
            testSet3.append(i)

    with open('Training_set.csv','rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in dataset:
            trainingSet3.append(i)


    #print(testSet3)
    #print(trainingSet3)
    #sys.exit(0)
    #print('Train set: ' + repr(len(trainingSet)))
    #print('Test set: ' + repr(len(testSet)))
    # generate predictions
    predictions = []
    count += 1
    k = 3
    count += 1
    for x in range(len(testSet3)):
        neighbors = getNeighbors(trainingSet3, testSet3[x], k)
        count += 1
        result = getResponse(neighbors)
        count += 1
        predictions.append(result)
        count += 1
        # print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet3, predictions)
    count += 1
    #print('Accuracy: ' + repr(accuracy) + '%')
    #print('Counts = ' + str(count))
    print(repr(len(trainingSet3)) + "," + repr(len(testSet3)) + "," + repr(accuracy) + "," + str(count))

    # User input is the first row of the .csv
    #inputFile = 'input.csv' 
    #loadDataset(inputFile, split, trainingSet2, testSet2)
    #print(trainingSet2)
    #sys.exit(0)
    userInput = [1, 60, 1, 65, 8450, 1, 0, 1, 1, 1, 208500, "200000-299999"]

    #uNeighbors = getNeighbors(trainingSet, userInput, k)
    #uResult = getResponse(uNeighbors)
    #print("Expected value - Close to 200000-299999")
    #print("User Input Prediction = " + uResult)
    #print("User Input Actual = " + userInput[10])

main('clean.csv')
