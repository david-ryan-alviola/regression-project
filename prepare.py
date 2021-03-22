import env

from utilities import split_dataframe_continuous_target, generate_xy_splits

def _clean_zillow(df):
    zillow_df = df.copy()
    
    zillow_df = zillow_df.rename(columns={'bathroomcnt' : 'bathrooms', 'bedroomcnt' : 'bedrooms', 'calculatedfinishedsquarefeet' : 'total_sqft', 'taxvaluedollarcnt' : 'tax_value', 'taxamount' : 'tax_amount'})
    
    return _remove_outliers(zillow_df)
    
def _remove_outliers(zillow_df):
    
    # Bathroom outliers
    upper_bath, lower_bath = _generate_outlier_bounds(zillow_df, 'bathrooms')

    # Bedroom outliers
    upper_beds, lower_beds = _generate_outlier_bounds(zillow_df, 'bedrooms')
    
    # Sqft outliers
    upper_sqft, lower_sqft = _generate_outlier_bounds(zillow_df, 'total_sqft')
    
    # Tax value outliers
    upper_value, lower_value = _generate_outlier_bounds(zillow_df, 'tax_value')
    
    non_outliers = (zillow_df.bathrooms > lower_bath) & (zillow_df.bathrooms < upper_bath) & (zillow_df.bedrooms > lower_beds) & (zillow_df.bedrooms < upper_beds) & (zillow_df.total_sqft > lower_sqft) & (zillow_df.total_sqft < upper_sqft) & (zillow_df.tax_value > lower_value) & (zillow_df.tax_value < upper_value)
    
    return zillow_df[non_outliers]

def _generate_outlier_bounds(df, column, multiplier=1.5):
    q1 = df[column].quantile(.25)
    q3 = df[column].quantile(.75)
    iqr = q3 - q1

    upper = q3 + (multiplier * iqr)
    lower = q1 - (multiplier * iqr)
    
    return upper, lower

def prepare_zillow(unprepared_zillow):
    prepped_data = {}
    
    prepped_data['population'] = _clean_zillow(unprepared_zillow)
    prepped_data['samples'] = split_dataframe_continuous_target(prepped_data['population'], 'tax_value')
    
    return prepped_data 