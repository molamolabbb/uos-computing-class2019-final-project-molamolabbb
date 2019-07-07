# Final-project 
### Jua Kim

## Datas
I used a iris_data in sckit-learn.
<br/>
The number of iris data is 150.
<br/>
so i seperate the data; train : 100, test :50.


### Data information
0 : 'setosa'
<br/>
1 : 'versicolor'
<br/>
2 : 'virginica'
<br/>

| __variables__ |
|---------------|
| sepal length  |
| sepal width   | 
| petal length  | 
| petal width   |  

4 dimension

## Machine learning technique : Random Forest
I choose the __random forest__ to predict the kind of iris.
First, load the iris data and make random samples.
Second, separate the test(50) and train datas(100). 
and then, make trees(random_forest) with train_data with step. The more steps, the bigger trees(the less # of trees).
Random forest makes several decision trees randomly. 
forest_classifier take votes with trees and counts how many vote they get.
Finally, we can get the accuracy checking test labels and votes.
I can see the result changing the step. 
<br/>
This method can be reduce overtraining.
<br/>

## result
I got about 97% accuracy.
If a tree is too big, its accuracy reduces.
