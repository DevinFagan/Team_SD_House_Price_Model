def ordinal_ranker(housedf):
    '''
    converts ordinal rankings in Ames houseprice files to numerics
    input is dataframe after fxn that removes NAs in non-ordinal ranking columns
    all ordinals are squared integers, *best* is highest value
    output goes to function for feature removal
    '''
    import pandas as pd
    import numpy as np
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



