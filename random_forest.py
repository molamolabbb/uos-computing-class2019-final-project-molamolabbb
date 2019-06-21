from tree import *
import random 
import collections

def open_csv(input_file):
    data_ls = []
    with open(input_file, 'r', newline='') as filereader :
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            data_ls.append(row_list)    
    return data_ls

def make_trees(datas,data,label,step):
    trees = []
    for i in range(0,int(len(datas)/step)*step,step):
        tree = build_tree_id3(datas[i:i+step],100)
        trees.append(tree)
        tree_accuracy(tree,data,label)
    return trees

def forest_classify(trees, inputs):
    votes = [classify(tree, inputs) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]

if __name__ == "__main__":
    new_train = open_csv('titanic/train_new.csv')
    train_data = list([[float(di) for di in d[2:]] for d in new_train])
    train_label = list([int(d[1]) for d in new_train])
    train_datas = []
    for d,i in zip(train_data,train_label):
        d = tuple(d)
        train_datas.append(((d),i))

    new_test = open_csv('titanic/test_new.csv')
    test_data = list([[float(di) for di in d[1:]] for d in new_test])
    label_test = open_csv('titanic/gender_submission.csv')
    test_label = list([int(d[1]) for d in label_test])

    # titanic gender submission
    for i in range(1,10):
        trees = make_trees(train_datas,train_data,train_label,i)
        classifier = [forest_classify(trees,inputs) for inputs in test_data]
        k = 0
        for label, val in zip(test_label,classifier):
            if label == val:
                k+=1
        print(k*100/len(test_label))
