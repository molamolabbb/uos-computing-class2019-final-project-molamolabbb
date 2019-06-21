# Final-project : Who will be the Survivor? 
### Jua Kim

## Datas
This is Titanic survivor data from kaggle (Very Well-known!).
The data separated two, one is __training set__ and the other is __test set__.
Both data sets include features of the passengers(like sex, age, ticket-class...).
<br/>
The differences of data sets are training set has survival and the other has not.
<br/>
but they give the gender_submission.csv.
This is a set of predictions that assume all and only female passengers survive.
so i checked this data to calculate the accuracy.


### Data information
I manufactured the kaggle datas because don't need variables.
Here is the Variables i used.

| __variables__ | __Definition__ | meaning of the number |
|---------------|----------------|-----------------------|
| survival      | Survival       | 0 = NO, 1 = Yes       |
| pclass        | Ticket class   |1 = 1st, 2 = 2nd, 3 = 3rd|
| sex           |     Sex        |  male = 0, female = 1 |
| age           |  age           |missig value = mean value(29.6)|
| sibsp         | the number of siblings/spouses abroad the titanic||
| parch         | the number of parents/children abroad the titanic ||
| fare          | Passenger fare | |
| embarked      | Port of embarkation | Southampton = 0, Cherbourg = 1, Queenstown = 2|

## Machine learning technique : Random Forest
I choose the __random forest__ to predict the survivor. 
I made the random forest to upgrade the decision trees(last time i made).
Random forest makes several decision trees randomly, and have them "vote" on the output.
This method can be reduce overtraining.
<br/>
_Several normal people are better than 1 smart person!_
<br/>
![alt text](https://www.researchgate.net/profile/Evaldas_Vaiciukynas/publication/301638643/figure/fig1/AS:355471899807744@1461762513154/Architecture-of-the-random-forest-model.png)
<br/>
## result

I run the random forest in this data.
I got 94% accuracy to predict the survivor. 
and It is much better than 1 big trees' accuracy(89%)!

## Errors
1.
When I process make_trees(), If step > 12 , I got an error below.
<br/>
 `UnboundLocalError: local variable 'threshold_' referenced before assignment`
<br/>
I don't know why i get this error.
<br/>
2. 
I have done random and separate training data. But when check the accuracy, i got a very bad accuracy.
so i can't uploaded.
