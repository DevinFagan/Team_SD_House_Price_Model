def ordinal_ranker(housedf):
#  making assumption all public utilities is best/highest
    utility_map_dict = {'allpub':4,'nosewr':3,'nosewa':2,'elo':1}
    housedf['Utilities'] = housedf['Utilities'].str.lower()
    housedf['Utilities'] = housedf['Utilities'].replace(utility_map_dict)
# assume gentle slope is best/highest
    lnd_slp_map_dict = {'gtl':4,'mod':3,'sev':2}
    housedf['LandSlope'] = housedf['LandSlope'].str.lower()
    housedf['LandSlope'] = housedf['LandSlope'].replace(lnd_slp_map_dict)
 # Exterior Quality, assume Exc is best/highest
    ext_qual_map_dict = {'ex':5,'gd':4,'ta':3,'fa':2,'po':1}
    housedf['ExterQual'] = housedf['ExterQual'].str.lower()
    housedf['ExterQual'] = housedf['ExterQual'].replace(ext_qual_map_dict)
 # Exterior Condition, assume Exc is best/highest
 # reuse exterior quality map
    housedf['ExterCond'] = housedf['ExterCond'].str.lower()
    housedf['ExterCond'] = housedf['ExterCond'].replace(ext_qual_map_dict)
 # Basement Quality, assume Exc is best/highest
    bsmt_qual_map_dict = {'ex':6,'gd':5,'ta':4,'fa':3,'po':2}
    housedf['BsmtQual'] = housedf['BsmtQual'].str.lower()
    housedf['BsmtQual'] = housedf['BsmtQual'].replace(bsmt_qual_map_dict)
    housedf['BsmtQual'] = housedf['BsmtQual'].fillna(1)
 # Basement Condition, assume Exc is best/highest, fill na with 1
 # reuse bsmt quality map
    housedf['BsmtCond'] = housedf['BsmtCond'].str.lower()
    housedf['BsmtCond'] = housedf['BsmtCond'].replace(bsmt_qual_map_dict)
    housedf['BsmtCond'] = housedf['BsmtCond'].fillna(1)
 # Basement Exposure, assume Gd is best/highest, fill na with 1
    bsmt_exp_map_dict = {'gd':5,'av':4,'mn':3,'no':2}
    housedf['BsmtExposure'] = housedf['BsmtExposure'].str.lower()
    housedf['BsmtExposure'] = housedf['BsmtExposure'].replace(bsmt_exp_map_dict)
    housedf['BsmtExposure'] = housedf['BsmtExposure'].fillna(1)
 # Basement Finish Type, assume GLQ is best/highest, fill na with 1
    bsmt_finish_map_dict = {'glq':7,'alq':6,'blq':5,'rec':4,'lwq':3,'unf':2}
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].str.lower()
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].replace(bsmt_finish_map_dict)
    housedf['BsmtFinType1'] = housedf['BsmtFinType1'].fillna(1)
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].str.lower()
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].replace(bsmt_finish_map_dict)
    housedf['BsmtFinType2'] = housedf['BsmtFinType2'].fillna(1)
 # Electrical system, assume SBrkr is best/highest
    electrical_map_dict = {'sbrkr':4,'fusea':3,'fusef':2,'mix':2,'fusep':1}
    housedf['Electrical'] = housedf['Electrical'].str.lower()
    housedf['Electrical'] = housedf['Electrical'].replace(electrical_map_dict)
    housedf['Electrical'] = housedf['Electrical'].fillna(0) #shouldn't need this
 # FireplaceQuality, assume Ex is best/highest, fill na with 1
#   reuse bsmt quality map, same scale
    housedf['FireplaceQu'] = housedf['FireplaceQu'].str.lower()
    housedf['FireplaceQu'] = housedf['FireplaceQu'].replace(bsmt_qual_map_dict)
    housedf['FireplaceQu'] = housedf['FireplaceQu'].fillna(1)
 # Garage finish, assume Fin is best/highest, fill na with 1
    gar_fin_map_dict = {'fin':4,'rfin':3,'unf':2} #fill na with 1
    housedf['GarageFinish'] = housedf['GarageFinish'].str.lower()
    housedf['GarageFinish'] = housedf['GarageFinish'].replace(gar_fin_map_dict)
    housedf['GarageFinish'] = housedf['GarageFinish'].fillna(1)    
 # Garage Quality, assume Ex is best/highest, fill na with 1
 # reuse bsmt quality map, same scale
    housedf['GarageQual'] = housedf['GarageQual'].str.lower()
    housedf['GarageQual'] = housedf['GarageQual'].replace(bsmt_qual_map_dict)
    housedf['GarageQual'] = housedf['GarageQual'].fillna(1)
 # Garage Condition, assume Ex is best/highest, fill na with 1
 # reuse bsmt quality map, same scale
    housedf['GarageCond'] = housedf['GarageCond'].str.lower()
    housedf['GarageCond'] = housedf['GarageCond'].replace(bsmt_qual_map_dict)
    housedf['GarageCond'] = housedf['GarageCond'].fillna(1)
 # Paved drive, assume Paved(Y) is best/highest
    pave_drv_map_dict = {'y':3,'p':2,'n':1}
    housedf['PavedDrive'] = housedf['PavedDrive'].str.lower()
    housedf['PavedDrive'] = housedf['PavedDrive'].replace(bsmt_qual_map_dict)
    housedf['GarageCond'] = housedf['GarageCond'].fillna(1)
    return housedf