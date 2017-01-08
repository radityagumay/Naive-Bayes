import csv
## http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/


def loadData(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


filename = "data.csv"
dataset = loadData(filename)
print ('loaded data file {0} with {1} rows').format(filename, len(dataset))
