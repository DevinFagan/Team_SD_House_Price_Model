def model_coefs (data, model):
    import pandas as pd
    from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, ElasticNetCV
    ames_prices = data.loc[:,"SalePrice"]
    ames_feats = data.drop(columns = "SalePrice")
    names = ames_feats.columns
    if model not in ['lasso', 'ridge', 'elasticnet']:
        raise ValueError("%s not in model choices" %(model))
    if model == "lasso":
        model = Lasso(alpha=0.0007,normalize = True,copy_X=True,selection='cyclic',max_iter=100000)
    if model == "ridge":
        model = Ridge(normalize = True)
    if model == "elasticnet":
        model = ElasticNet(alpha=0.0007, l1_ratio=0.3, 
            fit_intercept=True, normalize=True, precompute=False, 
            max_iter=100000, copy_X=True, tol=0.0001, warm_start=False, 
            positive=False, random_state=None, selection='cyclic')
    model.fit(ames_feats,ames_prices)
    results = pd.DataFrame(model.coef_).transpose()
    results.columns = names.tolist()
    results['intercept'] = model.intercept_
    results['score'] = model.score(ames_feats, ames_prices)
    results = results.transpose()
    results.columns = ['coefficients']
    return results


