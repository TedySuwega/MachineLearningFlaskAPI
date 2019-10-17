
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

import dataPrep

X_train = dataPrep.X_train
y_train = dataPrep.y_train
X_test = dataPrep.X_test
y_test = dataPrep.y_test


Xred = dataPrep.X_trainRed
yred = dataPrep.y_trainRed
XredT = dataPrep.X_testRed
yredT = dataPrep.y_testRed

#create model

clf = RandomForestClassifier()
clf.fit(X_train,y_train)

#result train and test
Score = clf.score(X_train,y_train)
testS = clf.score(X_test,y_test)
print('train : ',Score)
print('test : ',testS)

# find features importances
importances = pd.DataFrame(clf.feature_importances_,
                           index= X_train.columns,
                           columns=
                           ['importances']).sort_values('importances',
                                                        ascending=False)
print('features importance : \n',importances)


# preict test
print('==============')
onedata = X_train.loc[1,:]
intFeatures = onedata

predict = clf.predict([onedata])

""" Save model """
pickle.dump(clf,open('model.pkl','wb'))

""" load model """
model = pickle.load( open('model.pkl','rb'))

