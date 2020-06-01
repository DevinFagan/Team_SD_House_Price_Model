from ordinal_ranker import *
from fillna import *
import pandas as pd
import numpy as np
import csv
import statistics

from sklearn import model_selection as ms
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, ElasticNetCV
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

##READ DATA
house_price = pd.read_csv('train.csv')
house_test = pd.read_csv('test.csv')
house_train = house_price.drop('SalePrice',axis =1)
data = pd.concat([house_train, house_test])

## DATA Preprocessing
# call overall preprocessing fxn from fillna
data = data_process(data)

# save data after preprocessing
data.to_csv('cleaned_all_data.csv')

# break data file back apart into training and submission data set
train = data.iloc[:house_price.shape[0],:]
test = data.iloc[house_price.shape[0]:,:]


## separate the predictors and response in the training data set
x_train = np.array(train)
y_train = np.log(np.ravel(house_price['SalePrice']))


## split data into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(x_train, y_train, test_size=0.2)


## train

## set model
# lasso
lasso = Lasso(normalize = True)

# ridge
ridge = Ridge(normalize = True)

# elasticnet
elasticnet = ElasticNet(normalize = True)

# SVR regression
svr = SVR()
svr.set_params(C= 0.045, epsilon = 0.06, kernel = 'linear')

# Gradient Boosting Regressor
gbr = GradientBoostingRegressor(n_estimators=6000,
                                learning_rate=0.01,
                                max_depth=4,
                                max_features='sqrt',
                                min_samples_leaf=15,
                                min_samples_split=10,
                                loss='huber',
                                random_state=42) 

#Random Forest Regressor
randomForest= RandomForestRegressor(n_estimators=1200, max_depth=15,
                          min_samples_split=5,
                          min_samples_leaf=5,
                          max_features=None,
                          oob_score=True,
                          random_state=42)

#train models and test
def cv_score(model, X_train = X_train,Y_train = Y_train, X_test = X_test,Y_test = Y_test):
    if model not in ['lasso', 'ridge', 'elasticnet','svr','randomForest','gbr']:
        raise ValueError("%s not in model choices" %(model))
    model.fit(X_train, Y_train)
    score_train = model.score(X_train, Y_train)
    score_test = model.score(X_test, Y_test)
    return score_train, score_test

def predict(model, test = test):
    return model.predict(test)


model_list = [lasso, ridge, elasticnet,svr,randomForest,gbr]
model_scores_tr = {model:cv_score(model)[0] for model in model_list}
model_scores_tt = {model:cv_score(model)[1] for model in model_list}

#compare scores
train_score_lists = model_scores_tr.values()
test_score_lists = model_scores_tt.values() 
model_lists = [type(model).__name__ for model in model_list]
model_lists[3:] = ['SVR','RF','GBR']
x = list(zip(model_lists,train_score_lists)) # unpack a list of pairs into two tuples
y = list(zip(model_lists,test_score_lists))
plt.plot(*zip(*x),label='train')
plt.plot(*zip(*y),label='test')
plt.ylim((0.5, 1))
plt.title('Comparsion of R-square')

plt.show()

