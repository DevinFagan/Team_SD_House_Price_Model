#  script to run anovas to find potential correlations between categoricals and continuous
# import necessary functions
from ordinal_ranker import *
from fillna import *
import pandas as pd
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# read in training data file
house_price = pd.read_csv('train.csv')

# random imputation to fill in NAs
fillna(house_price)

# change ordinal rankings into continuous, and change to quadratic
ordinal_ranker(house_price)

# change names of columns that begin with numbers
house_price.rename(columns = {'1stFlrSF':'FirstFlrSF','2ndFlrSF':'SecndFlrSF',\
                              '3SsnPorch':'ThreSsnPorch'}, inplace = True)
# create lists of columns that are categorical vs continous to do anovas
house_price_str = house_price.select_dtypes(exclude='number').columns
house_price_num = house_price.select_dtypes(include='number').columns

# run through all continuous columns for each categorical
for numi in house_price_num:
    for strj in house_price_str:
        d = numi+'~'+strj
        try :
            mod = ols(d, data= house_price).fit()
            aov_table = sm.stats.anova_lm(mod, typ=2)
# We are dividing the sums of squares divided by the total error, in an analog to an R2
            if (100*aov_table.iloc[0,0]/(aov_table.iloc[0,0] + aov_table.iloc[1,0]))>50:
                print(numi,' ',strj)
                print((aov_table.iloc[0,0]/(aov_table.iloc[0,0] + aov_table.iloc[1,0]))**0.5)
            else:
                pass
        except:
# we do have some variables where we have only one observation for a group, which breaks anova
            print(numi,' ',strj,' min grp size')
            f = house_price[[numi,strj]].groupby(strj).count()
            print(min(f[numi]))