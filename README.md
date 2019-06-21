# Final-project : Who will be the Survivor? 
## Jua Kim

## Datas
This is Titanic survivor data from kaggle (Very Well-known!).
The data separated two, one is __training set__ and the other is __test set__.
Both data sets include features of the passengers(like sex, age, ticket-class...).
\n
The differences of data sets are training set has survival and the other has not.
Only kaggle site i can check the test set, so i separate training set, one i used training set and the other i used test set.
\n
but they give the gender_submission.csv.
This is a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.
so i checked this data to calculate the accuracy.


### Data information
I manufactured the kaggle datas because don't need variables.
Here is the Variables i used.

| __variables__ | __Definition__ | meaning of the number |
|---------------|----------------|-----------------------|
| survival      | Survival       | 0 = NO, 1 = Yes       |
| pclass        | Ticket class   |1 = 1st,2 = 2nd,3 = 3rd|
| sex           |     Sex        |  male = 0, female = 1 |
| age           |  age           |missig value = mean value(29.6)|
| sibsp         | the number of siblings/spouses abroad the titanic||
| parch         | the number of parents/children abroad the titanic ||
| fare          | Passenger fare | |
| embarked      | Port of embarkation | Southampton = 0, Cherbourg = 1, Queenstown = 2|




