import env

from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score

def generate_baseline_model(prediction, key_name, target, y_train, y_validate):
    y_train[key_name] = prediction
    y_validate[key_name] = prediction
    
    rmse_train, rmse_validate = _calculate_rmse_values(target, key_name, y_train, y_validate)

    _print_rmse_comparison(rmse_train, rmse_validate, key_name)
    _print_train_and_validate_evals(y_train, y_validate, target, key_name)
    
def generate_regression_model(regressor, X_train, X_validate, y_train, y_validate, key_name, target):
    regressor.fit(X_train, y_train[target])

    y_train[key_name] = regressor.predict(X_train)
    y_validate[key_name] = regressor.predict(X_validate)
    
    rmse_train, rmse_validate = _calculate_rmse_values(target, key_name, y_train, y_validate)
    
    _print_rmse_comparison(rmse_train, rmse_validate, key_name)
    _print_train_and_validate_evals(y_train, y_validate, target, key_name)
    
    return regressor
    
def apply_model_to_test_data(model, X_test, y_test, key_name, target):
    y_test[key_name] = model.predict(X_test)

    rmse_test = sqrt(mean_squared_error(y_test[target], y_test[key_name]))

    print(f"RMSE for {key_name} model\nOut-of-Sample Performance: {rmse_test}")
    _print_rsquare_and_variance(y_test, target, key_name)
    
def _calculate_rmse_values(target, key_name, y_train, y_validate):
    rmse_train = sqrt(mean_squared_error(y_train[target], y_train[key_name]))
    rmse_validate = sqrt(mean_squared_error(y_validate[target], y_validate[key_name]))
    
    return rmse_train, rmse_validate

def _print_rmse_comparison(rmse_train, rmse_validate, key_name):
    print(f"RMSE using {key_name}\nTrain/In-Sample: ", round(rmse_train, 4), 
          "\nValidate/Out-of-Sample: ", round(rmse_validate, 4))
    
def _print_rsquare_and_variance(y_df, target, key_name):
    evs = explained_variance_score(y_df[target], y_df[key_name])
    r2 = r2_score(y_df[target], y_df[key_name])
    
    print(f"Explained variance:  {round(evs, 4)}")
    print(f"R-squared value:  {round(r2, 4)}")
    
def _print_train_and_validate_evals(y_train, y_validate, target, key_name):
    print("--------------------------------------------------")
    print("Train")
    _print_rsquare_and_variance(y_train, target, key_name)
    print("--------------------------------------------------")
    print("Validate")
    _print_rsquare_and_variance(y_validate, target, key_name)
                        