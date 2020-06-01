def ordinal_ranker(housedf):
    '''
    converts ordinal rankings in Ames houseprice files to numerics
    input is dataframe after fxn that removes NAs in non-ordinal ranking columns
    all ordinals are squared integers, *best* is highest value
    output goes to function for feature removal
    '''
    import pandas as pd
    import numpy as np
    import random
    random.seed(8)
 #  assume all public utilities is best/highest, assume NA is ELO
    utility_map_dict = {'allpub':16,'nosewr':9,'nosewa':4,'elo':1}
    housedf['Utilities'] = housedf['Utilities'].str.lower()
    housedf['Utilities'] = housedf['Utilities'].replace(utility_map_dict)
    housedf['Utilities'] = housedf['Utilities'].fillna(1)
 # assume gentle slope is best/highest, assume NA is gentle since it's Iowa
    lnd_slp_map_dict = {'gtl':9,'mod':4,'sev':1}
    housedf['LandSlope'] = housedf['LandSlope'].str.lower()
    housedf['LandSlope'] = housedf['LandSlope'].replace(lnd_slp_map_dict)
    housedf['LandSlope'] = housedf['LandSlope'].fillna(9)
 # Exterior Quality, assume Exc is best/highest, assume NA is ta
    ext_qual_map_dict = {'ex':25,'gd':16,'ta':9,'fa':4,'po':1}
    housedf['ExterQual'] = housedf['ExterQual'].str.lower()
    housedf['ExterQual'] = housedf['ExterQual'].replace(ext_qual_map_dict)
    housedf['ExterQual'] = housedf['ExterQual'].fillna(9)
 # Exterior Condition, assume Exc is best/highest
 # reuse exterior quality map
    housedf['ExterCond'] = housedf['ExterCond'].str.lower()
    housedf['ExterCond'] = housedf['ExterCond'].replace(ext_qual_map_dict)
    housedf['ExterCond'] = housedf['ExterCond'].fillna(9)
 # Basement Quality, assume Exc is best/highest
    bsmt_qual_map_dict = {'ex':36,'gd':25,'ta':16,'fa':9,'po':4}
    housedf['BsmtQual'] = housedf['BsmtQual'].str.lower()
    housedf['BsmtQual'] = housedf['BsmtQual'].replace(bsmt_qual_map_dict)
    housedf['BsmtQual'] = housedf['BsmtQual'].fillna(1)
 # Basement Condition, assume Exc is best/highest, fill no bsmt/na with 1
 # reuse bsmt quality map
    housedf['BsmtCond'] = housedf['BsmtCond'].str.lower()
    housedf['BsmtCond'] = housedf['BsmtCond'].replace(bsmt_qual_map_dict)
    housedf['BsmtCond'] = housedf['BsmtCond'].fillna(1)
 # Basement Exposure, assume Gd is best/highest, fill no bsmt/na with 1
    bsmt_exp_map_dict = {'gd':25,'av':16,'mn':9,'no':4}
    housedf['BsmtExposure'] = housedf['BsmtExposure'].str.lower()
    housedf['BsmtExposure'] = housedf['BsmtExposure'].replace(bsmt_exp_map_dict)
    housedf['BsmtExposure'] = housedf['BsmtExposure'].fillna(1)
 # Basement Finish Type, assume GLQ is best/highest, fill no bsmt/na with 1
    bsmt_finish_map_dict = {'glq':49,'alq':36,'blq':25,'rec':16,'lwq':9,'unf':4}
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].str.lower()
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].replace(bsmt_finish_map_dict)
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].fillna(1)
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].str.lower()
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].replace(bsmt_finish_map_dict)
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].fillna(1)
 # Electrical system, assume SBrkr is best/highest, fill na with 3
    electrical_map_dict = {'sbrkr':16,'fusea':9,'fusef':4,'mix':4,'fusep':1}
    housedf['Electrical'] = housedf['Electrical'].str.lower()
    housedf['Electrical'] = housedf['Electrical'].replace(electrical_map_dict)
    housedf['Electrical'] = housedf['Electrical'].fillna(9) 
 # FireplaceQuality, assume Ex is best/highest, fill no frplc/na with 1
 # reuse bsmt quality map, same scale
    housedf['FireplaceQu'] = housedf['FireplaceQu'].str.lower()
    housedf['FireplaceQu'] = housedf['FireplaceQu'].replace(bsmt_qual_map_dict)
    housedf['FireplaceQu'] = housedf['FireplaceQu'].fillna(1)
 # Garage finish, assume Fin is best/highest, fill no grge/na with 1
    gar_fin_map_dict = {'fin':16,'rfn':9,'unf':4} 
    housedf['GarageFinish'] = housedf['GarageFinish'].str.lower()
    housedf['GarageFinish'] = housedf['GarageFinish'].replace(gar_fin_map_dict)
    housedf['GarageFinish'] = housedf['GarageFinish'].fillna(1)    
 # Garage Quality, assume Ex is best/highest, fill no grge/na with 1
 # reuse bsmt quality map, same scale
    housedf['GarageQual'] = housedf['GarageQual'].str.lower()
    housedf['GarageQual'] = housedf['GarageQual'].replace(bsmt_qual_map_dict)
    housedf['GarageQual'] = housedf['GarageQual'].fillna(1)
 # Garage Condition, assume Ex is best/highest, fill no grge/na with 1
 # reuse bsmt quality map, same scale
    housedf['GarageCond'] = housedf['GarageCond'].str.lower()
    housedf['GarageCond'] = housedf['GarageCond'].replace(bsmt_qual_map_dict)
    housedf['GarageCond'] = housedf['GarageCond'].fillna(1)
 # Paved drive, assume Paved(Y) is best/highest, fill na with 3
    pave_drv_map_dict = {'y':9,'p':4,'n':1}
    housedf['PavedDrive'] = housedf['PavedDrive'].str.lower()
    housedf['PavedDrive'] = housedf['PavedDrive'].replace(pave_drv_map_dict)
    housedf['PavedDrive'] = housedf['PavedDrive'].fillna(3)
 # Pool quality, assume Ex is highest/best, fill no pool/na with 1
    pool_qc_map_dict = {'ex':25,'gd':16,'ta':9, 'fa':4}
    housedf['PoolQC'] = housedf['PoolQC'].str.lower()
    housedf['PoolQC'] = housedf['PoolQC'].replace(pool_qc_map_dict)
    housedf['PoolQC'] = housedf['PoolQC'].fillna(1)
 # Fence quality, assume GdPrv/GdWo is best/highest, fill no fence/na with 1
    fence_qc_map_dict = {'mnww': 4,'mnprv': 4,'gdwo': 9,'gdprv':9}
    housedf['Fence'] = housedf['Fence'].str.lower()
    housedf['Fence'] = housedf['Fence'].replace(fence_qc_map_dict)
    housedf['Fence'] = housedf['Fence'].fillna(1)
 # Overall quality, 10 is best, highest, need to fill in any NAs
    overll_map_dict = {10:100, 9:81, 8:64, 7:49, 6:36, 5:25, 4:16, 3:9, 2:4}
    housedf['OverallQual'] = housedf['OverallQual'].replace(overll_map_dict)
    housedf.loc[housedf['OverallQual'].isnull(), 'OverallQual'] = \
            housedf.OverallQual.dropna().sample(housedf['OverallQual'].\
            isnull().sum()).values
 # Overall condition, 10 is best/highest, random impute to fill in any NAs
  # reuse overll_map_dict
    housedf['OverallCond'] = housedf['OverallCond'].replace(overll_map_dict)
    housedf.loc[housedf['OverallCond'].isnull(), 'OverallCond'] = \
            housedf.OverallCond.dropna().sample(housedf['OverallCond'].\
            isnull().sum()).values
 # LotShape, assume Reg is highest/best, fill in NAs with 4/regular
    lot_shp_map_dict = {'reg': 16,'ir1': 9,'ir2': 4,'ir3':1}
    housedf['LotShape'] = housedf['LotShape'].str.lower()
    housedf['LotShape'] = housedf['LotShape'].replace(lot_shp_map_dict)
    housedf['LotShape'] = housedf['LotShape'].fillna(16)  
 # KitchenQual, assume Ex is highest/best, fill in NAs with random impute
    # reuse basement quality map, same scale
    housedf['KitchenQual'] = housedf['KitchenQual'].str.lower()
    housedf['KitchenQual'] = housedf['KitchenQual'].replace(bsmt_qual_map_dict)
    housedf.loc[housedf['KitchenQual'].isnull(), 'KitchenQual'] = \
            housedf.KitchenQual.dropna().sample(housedf['KitchenQual'].\
            isnull().sum()).values
 # Functional, assume typ is highest/best, fill in NAs with random inpute
    fdxl_map_dict = {'typ': 64,'min1': 49,'min2': 36,'mod':25,'maj1':16,'maj2':9,'sev':4,'sal':1}
    housedf['Functional'] = housedf['Functional'].str.lower()
    housedf['Functional'] = housedf['Functional'].replace(fdxl_map_dict) 
    housedf.loc[housedf['Functional'].isnull(), 'Functional'] = \
            housedf.Functional.dropna().sample(housedf['Functional'].\
            isnull().sum()).values
    return housedf

def feature_select(housedf):
    # rename features with names that begin with number.  OLS anova had trouble
    housedf.rename(columns = {'1stFlrSF':'FirstFlrSF','2ndFlrSF':'SecndFlrSF',\
                              '3SsnPorch':'ThreSsnPorch'}, inplace = True)
    # remove highly correlated variables, and some others like ID
    housedf = housedf.drop(columns=["GarageCond","GarageCars","PoolArea","OverallQual",\
        "Fireplaces","YearBuilt","BsmtFinType2","FirstFlrSF","TotRmsAbvGrd",\
        "MSSubClass","BldgType","HouseStyle","GarageType","GarageYrBlt","Id",\
        "MSSubClass"], inplace=True)
    return housedf

def value_check(housedf):
    import random
    random.seed(8)
    data_val_dict = {'MSZoning':['A','C','FV','I','RH','RL','RP','RM'],'Street':['Grvl','Pave'],'Alley':['Grvl','Pave','NA'],'LotShape':['Reg','IR1','IR2','IR3'],'LandContour':['Lvl','Bnk','HLS','Low'],'Utilities':['AllPub','NoSewr','NoSeWa','ELO'],'LotConfig':['Inside','Corner','CulDSac','FR2','FR3'],'LandSlope':['Gtl','Mod','Sev'],'Neighborhood':['Blmngtn','Blueste','BrDale','BrkSide','ClearCr','CollgCr','Crawfor','Edwards','Gilbert','IDOTRR','MeadowV','Mitchel','Names','NoRidge','NPkVill','NridgHt','NWAmes','OldTown','SWISU','Sawyer','SawyerW','Somerst','StoneBr','Timber','Veenker'],'Condition1':['Artery','Feedr','Norm','RRNn','RRAn','PosN','PosA','RRNe','RRAe'],'Condition2':['Artery','Feedr','Norm','RRNn','RRAn','PosN','PosA','RRNe','RRAe'],'BldgType':['1Fam','2FmCon','Duplx','TwnhsE','TwnhsI'],'HouseStyle':['1Story','1.5Fin','1.5Unf','2Story','2.5Fin','2.5Unf','SFoyer','SLvl'],'RoofStyle':['Flat','Gable','Gambrel','Hip','Mansard','Shed'],'RoofMatl':['ClyTile','CompShg','Membran','Metal','Roll','Tar&Grv','WdShake','WdShngl'],'Exterior1st':['AsbShng','AsphShn','BrkComm','BrkFace','CBlock','CemntBd','HdBoard','ImStucc','MetalSd','Other','Plywood','PreCast','Stone','Stucco','VinylSd','Wd Sdng','WdShing'],'Exterior2nd':['AsbShng','AsphShn','BrkComm','BrkFace','CBlock','CemntBd','HdBoard','ImStucc','MetalSd','Other','Plywood','PreCast','Stone','Stucco','VinylSd','Wd Sdng','WdShing'],'MasVnrType':['BrkCmn','BrkFace','CBlock','None','Stone'],'ExterQual':['Ex','Gd','TA','Fa','Po'],'ExterCond':['Ex','Gd','TA','Fa','Po'],'Foundation':['BrkTil','CBlock','PConc','Slab','Stone','Wood'],'BsmtQual':['Ex','Gd','TA','Fa','Po','NA'],'BsmtCond':['Ex','Gd','TA','Fa','Po','NA'],'BsmtExposure':['Gd','Av','Mn','No','NA'],'BsmtFinType1':['GLQ','ALQ','BLQ','Rec','LwQ','Unf','NA'],'BsmtFinType2':['GLQ','ALQ','BLQ','Rec','LwQ','Unf','NA'],'Heating':['Floor','GasA','GasW','Grav','OthW','Wall'],'HeatingQC':['Ex','Gd','TA','Fa','Po'],'CentralAir':['N','Y'],'Electrical':['SBrkr','FuseA','FuseF','FuseP','Mix'],'KitchenQual':['Ex','Gd','TA','Fa','Po'],'Functional':['Typ','Min1','Min2','Mod','Maj1','Maj2','Sev','Sal'],'FireplaceQu':['Ex','Gd','TA','Fa','Po','NA'],'GarageType':['2Types','Attchd','Basment','BuiltIn','CarPort','Detchd','NA'],'GarageFinish':['Fin','RFn','Unf','NA'],'GarageQual':['Ex','Gd','TA','Fa','Po','NA'],'GarageCond':['Ex','Gd','TA','Fa','Po','NA'],'PavedDrive':['Y','P','N'],'PoolQC':['Ex','Gd','TA','Fa','NA'],'Fence':['GdPrv','MnPrv','GdWo','MnWw','NA'],'MiscFeature':['Elev','Gar2','Othr','Shed','TenC','NA'],'SaleType':['WD','CWD','VWD','New','COD','Con','ConLw','ConLI','ConLD','Oth'],'SaleCondition':['Normal','Abnorml','AdjLand','Alloca','Family','Partial']}
    house_price_str = ['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities','LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2','BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st','Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation','BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2','Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual','Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual','GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature','SaleType', 'SaleCondition']
    for col in house_price_str:
        for lvl in housedf[col].unique():
            if lvl not in data_val_dict[col]:
                a =  [random.sample(data_val_dict[col],1) for x in list(housedf.loc[housedf[col]==lvl,col])]
                housedf.loc[housedf[col]==lvl,col] = a
    return housedf

