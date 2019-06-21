from random_forest import (make_trees,forest_classify)
from pytest import approx

def test_make_trees():
    datas1 = [((0,0,0,0),0),
     ((1,1,1,1),1),
     ((0,1,0,1),0),
     ((1,0,1,0),1)] 
    datas2 = [((3.0, 0.0, 22.0, 1.0, 0.0, 7.25, 0.0), 0),
 ((1.0, 1.0, 38.0, 1.0, 0.0, 71.2833, 1.0), 1),
 ((3.0, 1.0, 26.0, 0.0, 0.0, 7.925, 0.0), 1),
 ((1.0, 1.0, 35.0, 1.0, 0.0, 53.1, 0.0), 1),
 ((3.0, 0.0, 35.0, 0.0, 0.0, 8.05, 0.0), 0),
 ((3.0, 0.0, 29.6, 0.0, 0.0, 8.4583, 2.0), 0),
 ((1.0, 0.0, 54.0, 0.0, 0.0, 51.8625, 0.0), 0),
 ((3.0, 0.0, 2.0, 3.0, 1.0, 21.075, 0.0), 0),
 ((3.0, 1.0, 27.0, 0.0, 2.0, 11.1333, 0.0), 1),
 ((2.0, 1.0, 14.0, 1.0, 0.0, 30.0708, 1.0), 1)]
    data1 = [[0,0,0,0],
            [1,1,1,1],
            [0,1,0,1],
            [1,0,1,0]]
    data2 = [[3.0, 0.0, 22.0, 1.0, 0.0, 7.25, 0.0],
 [1.0, 1.0, 38.0, 1.0, 0.0, 71.2833, 1.0],
 [3.0, 1.0, 26.0, 0.0, 0.0, 7.925, 0.0],
 [1.0, 1.0, 35.0, 1.0, 0.0, 53.1, 0.0],
 [3.0, 0.0, 35.0, 0.0, 0.0, 8.05, 0.0],
 [3.0, 0.0, 29.6, 0.0, 0.0, 8.4583, 2.0],
 [1.0, 0.0, 54.0, 0.0, 0.0, 51.8625, 0.0],
 [3.0, 0.0, 2.0, 3.0, 1.0, 21.075, 0.0],
 [3.0, 1.0, 27.0, 0.0, 2.0, 11.1333, 0.0],
 [2.0, 1.0, 14.0, 1.0, 0.0, 30.0708, 1.0]]
    label1 = [0,1,0,1]
    label2 = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    
    assert make_trees(datas1,data1,label1,2)==[[(0, 0), 0, 1], [(0, 0), 0, 1]]
    assert make_trees(datas1,data1,label1,4)==[[(0, 0), 0, 1]]
    assert make_trees(datas2,data2,label2,10)==[[(1, 0.0), 0, 1]]
    
    
def test_forest_classify():
    datas1 = [((0,0,0,0),0),
     ((1,1,1,1),1),
     ((0,1,0,1),0),
     ((1,0,1,0),1)] 
    datas2 = [((3.0, 0.0, 22.0, 1.0, 0.0, 7.25, 0.0), 0),
 ((1.0, 1.0, 38.0, 1.0, 0.0, 71.2833, 1.0), 1),
 ((3.0, 1.0, 26.0, 0.0, 0.0, 7.925, 0.0), 1),
 ((1.0, 1.0, 35.0, 1.0, 0.0, 53.1, 0.0), 1),
 ((3.0, 0.0, 35.0, 0.0, 0.0, 8.05, 0.0), 0),
 ((3.0, 0.0, 29.6, 0.0, 0.0, 8.4583, 2.0), 0),
 ((1.0, 0.0, 54.0, 0.0, 0.0, 51.8625, 0.0), 0),
 ((3.0, 0.0, 2.0, 3.0, 1.0, 21.075, 0.0), 0),
 ((3.0, 1.0, 27.0, 0.0, 2.0, 11.1333, 0.0), 1),
 ((2.0, 1.0, 14.0, 1.0, 0.0, 30.0708, 1.0), 1)]
    data1 = [[0,0,0,0],
            [1,1,1,1],
            [0,1,0,1],
            [1,0,1,0]]
    data2 = [[3.0, 0.0, 22.0, 1.0, 0.0, 7.25, 0.0],
 [1.0, 1.0, 38.0, 1.0, 0.0, 71.2833, 1.0],
 [3.0, 1.0, 26.0, 0.0, 0.0, 7.925, 0.0],
 [1.0, 1.0, 35.0, 1.0, 0.0, 53.1, 0.0],
 [3.0, 0.0, 35.0, 0.0, 0.0, 8.05, 0.0],
 [3.0, 0.0, 29.6, 0.0, 0.0, 8.4583, 2.0],
 [1.0, 0.0, 54.0, 0.0, 0.0, 51.8625, 0.0],
 [3.0, 0.0, 2.0, 3.0, 1.0, 21.075, 0.0],
 [3.0, 1.0, 27.0, 0.0, 2.0, 11.1333, 0.0],
 [2.0, 1.0, 14.0, 1.0, 0.0, 30.0708, 1.0]]
    label1 = [0,1,0,1]
    label2 = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    
    test1 = [1,1,1,1]
    test2 = [0,0,0,0]
    
    trees = make_trees(datas1,data1,label1,4)
    
    assert forest_classify(trees,test1)==1
    assert forest_classify(trees,test2)==0