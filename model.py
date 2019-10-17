
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
print("predict" ,predict)
print(type(predict))

# pred = clf.predict_proba(X_test)
#
# y_true = y_test
# y_pred = predict
#
# y_pred_proba = pred

# print(len(X_test[0]))
# print('len y_pred : ',len(y_pred))
# print(y_pred)
# print('len y_true : ',len(y_true))
# print(y_true)
# print('len y_pproba: ',len(y_pred_proba))
# print(y_pred_proba)
# print('y_pred[2] : ',y_pred[2])
# print('y_test[2] : ',y_test[2])
# print('len_ predict : ',len(predict))

# for i in range(len(predict)):
#     if (predict[i] == y_true[i]):
#         benar =+1
#
# acc = benar/len(y_true)
# print('acc : ',acc)

# resulst convusion matric
# convMat = confusion_matrix(y_true,y_pred)
# tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
#
# print('tn: ',tn,'\nfp: ',fp,'\nfn: ',fn,'\ntp: ',tp)
# print( y_pred_proba)

# calculate manual acc
# print(y_test)
# y_actual = []
# for i,v in y_test.items():
#     print('value : ', v)
#     y_actual.append(v)
#
# benar = 0
# for i in range(len(y_pred)):
#     if y_actual[i] == y_pred[i]:
#         benar =+1
#
# acc = benar/len(y_pred)*100
# print('acc : ',acc)

#save model
# with open("rf_mdl4.mdl", "wb") as f_mdl:
#     pickle.dump(clf, f_mdl, pickle.HIGHEST_PROTOCOL)
#
# with open("rf_mdl2.mdl", "rb") as f_mdl:
#     clf_load = pickle.load(f_mdl)
#     print(str(clf_load))
#
# a = clf_load.predict(X_test)
# print(a)


""" Save model """
# pickle.dump(clf,open('model.pkl','wb'))

""" load model """
model = pickle.load( open('model.pkl','rb'))
# print(model.predict(onedata))
# print(model.score(X_train,y_train))
