import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn import feature_selection


# df = pd.read_csv('D:\MILO\Flask\\tableDataMix.csv',delimiter=",")

df = pd.read_csv('D:\MILO\Flask\Data.csv',delimiter=",")
print(df)

print(df.hist_current)

"""
new feature percentege
"""
# percentage = []
#
# for i in range(df.shape[0]):
#     percentage.append((df['hist_current'].iloc[0])/
#                       (df['hist_current'].iloc[i]
#                       +df['hist_xday'].iloc[i]
#                       +df['hist_30dpd'].iloc[i]
#                       +df['hist_60dpd'].iloc[i]
#                       +df['hist_npl'].iloc[i]))
# df['percentage'] = percentage
# df['percentage'].replace([np.inf, -np.inf], 0, inplace=True)



"""
rewrite Bad as 0 and Good as 1
"""
# replacements ={
#     'Good' : 1,
#     'Bad'  : 0
# }
# df['STATUS'].replace(replacements, inplace=True)
y = df['STATUS']

"""
set feature from selected dimension
"""
X = df[['hist_current',
        'hist_xday',
        'hist_30dpd',
        'hist_60dpd',
        'hist_npl',
        'percentage',
        'all_hist_current',
        'all_hist_xday',
        'all_hist_30dpd',
        'all_hist_60dpd',
        'all_hist_npl',
        'all_hist_percentage']]

print(X)

"""
combine features and Target
"""
dataUse = df[['hist_current',
              'hist_xday',
              'hist_30dpd',
              'hist_60dpd',
              'hist_npl',
              'STATUS']]

X_red = df[['hist_current',
            'hist_xday',
            'percentage',
            'all_hist_current',
            'all_hist_xday',
            'all_hist_percentage']]
"""
split data to 80% train and 20% test 
"""
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2)


X_trainRed, X_testRed, y_trainRed, y_testRed = train_test_split(
    X_red,y, test_size=0.2
)

print(X_train)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(X.corr(), vmin=-1, vmax=1)
# fig.colorbar(cax)

data = df[['hist_current',
        'hist_xday',
        'hist_30dpd',
        'hist_60dpd',
        'hist_npl',
        'percentage',
        'all_hist_current',
        'all_hist_xday',
        'all_hist_30dpd',
        'all_hist_60dpd',
        'all_hist_npl',
        'all_hist_percentage',
        'STATUS']]


persetile = data.quantile(.50)
# data._check_percentile()

# print(y_test)
# for i in range(len(y_test)):
#     print(y_test[1][i])

# data.to_csv('Data.csv')
print(data)
print(X)
print(y)