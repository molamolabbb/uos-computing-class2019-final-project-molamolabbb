from sklearn import datasets
import numpy as np
import random
from tree import *

def make_trees(datas,data,label,step):
    trees = []
    for i in range(0,int(len(datas)/step)*step,step):
        tree = build_tree_id3(datas[i:i+step],100)
        trees.append(tree)
        tree_accuracy(tree,data,label)
    return trees

def forest_classify(trees, inputs):
    votes = [classify(tree, inputs) for tree in trees]
    counts = {}
    for i in votes:
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1
    val = 0
    for i in counts.keys():
        if counts[i] > val:
            most_common = i
            val = counts[i]
    return most_common

if __name__ == "__main__":
    iris = datasets.load_iris()
    iris_data = [np.append(d,i) for d,i in zip(iris.data,iris.target)]

    random_sample = random.sample(iris_data,len(iris_data))
    random_data = list([float(di) for di in d[:-1]] for d in random_sample)
    random_label = list([int(d[4])for d in random_sample])

    test_sample = random_sample[:50]
    test_data = random_data[:50]
    test_label = random_label[:50]

    train_sample = random_sample[50:]
    train_data = random_data[50:]
    train_label = random_label[50:]

    train_datas = []
    for d,i in zip(train_data,train_label):
        d = tuple(d)
        train_datas.append(((d),i))

    # i is step.
    for i in range(1,40):
        trees = make_trees(train_datas,train_data,train_label,i)
        classifier = [forest_classify(trees,inputs) for inputs in test_data]
        k = 0
        for label, val in zip(test_label,classifier):
            if label == val:
                k+=1
        print(k*100/len(test_label))
