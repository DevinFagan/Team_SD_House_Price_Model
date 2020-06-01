%load_ext autoreload
%autoreload 2
from ordinal_ranker import *
from fillna import *

# Import modules into Python
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
plt.rcParams["text.usetex"] = False

# Load in the data and merge the sample submission with the test dataset
house_price = pd.read_csv('train.csv')
house_test = pd.read_csv('test.csv')
sub_ys=pd.read_csv('sample_submission.csv')
house_test = pd.merge(house_test,sub_ys,how = 'inner', on = 'Id')

# Log Transform SalePrice
house_price["SalePrice"] = np.log1p(house_price["SalePrice"])

# Drop SalePrice from the dataset and make it a Dependent Variable
house_price_target = house_price['SalePrice'].reset_index(drop=True)
house_price = house_price.drop(['SalePrice'], axis=1)
house_test = house_test.drop(['SalePrice'], axis=1)

# Concat the test and train dataset
data = pd.concat([house_price, house_test])

# Process the data
data = data_process(data)

Recreate the train and test set
train = data.iloc[:house_price.shape[0],:]
test = data.iloc[house_price.shape[0]:,:]

Scale all of the columns
x_scaled = (train-train.min(axis=0))/(train.max(axis=0)-train.min(axis=0))

#Seperate the train data using train test split
X_train, X_test, y_train, y_test = train_test_split(x_scaled, house_price_target, test_size=0.2, random_state=42)

#Ridge Model
ridge = Ridge(normalize=True)

ridge.fit(X_train,y_train)

ridge.score(X_train,y_train)

ridge.score(X_test,y_test)

# Lasso Model
lasso = Lasso(alpha=0.0007, normalize = True, selection = 'cyclic', max_iter=100000)

lasso.fit(X_train,y_train)

lasso.score(X_train,y_train)

lasso.score(X_test,y_test)

#ElasticNet Model
ENet = ElasticNet(alpha=0.0007, l1_ratio=0.3, fit_intercept=True, normalize=True, precompute=False, max_iter=100000, copy_X=True, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')

ENet.fit(X_train,y_train)

ENet.score(X_train,y_train)

ENet.score(X_test,y_test)