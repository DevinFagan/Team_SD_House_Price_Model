import pandas as pd
import numpy as np

# train_raw = pd.read_csv("train.csv",index_col="Id")
# test_raw  = pd.read_csv("test.csv",index_col="Id")

def fillna(data):
    #Alley - Replace NA by None
    data.Alley = data.Alley.fillna('None')
    
    #MSZoning - fill NA with random impute
    data.loc[data['MSZoning'].isnull(), 'MSZoning'] = data.LotFrontage.dropna().sample(data['MSZoning'].isnull().sum()).values
        
    #Exterior1st - fill NA with random impute
    data.loc[data['Exterior1st'].isnull(), 'Exterior1st'] = data.LotFrontage.dropna().sample(data['Exterior1st'].isnull().sum()).values
    
    #Exterior2nd - fill NA with random impute
    data.loc[data['Exterior2nd'].isnull(), 'Exterior2nd'] = data.LotFrontage.dropna().sample(data['Exterior2nd'].isnull().sum()).values
    
    #MasVnrType - replce na with None, MasVnrArea - replce na with 0
    data.MasVnrType = data.MasVnrType.fillna('None')
    data.MasVnrArea = data.MasVnrArea.fillna(0)

    # LotFrontage - Random impute
    data.loc[data['LotFrontage'].isnull(), 'LotFrontage'] = data.LotFrontage.dropna().sample(data['LotFrontage'].isnull().sum()).values

    #BsmtFinSF1 - fill NA with 0
    data.BsmtFinSF1 = data.BsmtFinSF1.fillna(0)
    
    # BsmtFinSF2 - fill  NA with 0
    data.BsmtFinSF2 = data.BsmtFinSF2.fillna(0)
    
    # BsmtUnfSF - fill NA with 0
    data.BsmtUnfSF = data.BsmtUnfSF.fillna(0)

    # TotalBsmtSF - fill NA with 0
    data.TotalBsmtSF = data.TotalBsmtSF.fillna(0)
    
    # BsmtFullBath - fill NA with 0
    data.BsmtFullBath = data.BsmtFullBath.fillna(0)
    
    # BsmtHalfBath -  fill NA with 0
    data.BsmtHalfBath = data.BsmtHalfBath.fillna(0)
    
    #GarageType - fill na with None
    data.GarageType = data.GarageType.fillna('None')
    
    # GarageArea -  fill NA with median
    data.GarageArea = data.GarageArea.fillna(data.GarageArea.median())

    # GarageCars -  fill NA with median
    data.GarageCars = data.GarageCars.fillna(data.GarageCars.median())
    
    #GarageYear - fill na with median of years
    data.GarageYrBlt = data.GarageYrBlt.fillna(data.GarageYrBlt.median())

    #Misc features - Change all to Yes and fill na with None
    data.MiscFeature = data.MiscFeature.replace(data.MiscFeature.dropna(),'Yes').fillna('None')
    
    # SaleType -  fill NA with random impute?
    data.loc[data['SaleType'].isnull(), 'SaleType'] = data.LotFrontage.dropna().sample(data['SaleType'].isnull().sum()).values

    return data, data.loc[:, data.isnull().any()] # check if NA exists

def dummy_conv(data):
    '''
    converts all categoricals to dummies
    input is dataframe
    output is non-mutating, need to set equal to function call
    '''
    return pd.get_dummies(data,drop_first=True)
