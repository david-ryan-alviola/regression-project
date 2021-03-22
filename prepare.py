import env

from utilities import split_dataframe_continuous_target, generate_xy_splits

def _clean_zillow(df):
    zillow_df = df.copy()
    
    zillow_df = zillow_df.rename(columns={'bathroomcnt' : 'bathrooms', 'bedroomcnt' : 'bedrooms', 'calculatedfinishedsquarefeet' : 'total_sqft', 'taxvaluedollarcnt' : 'tax_value', 'taxamount' : 'tax_amount'})
    
    return _remove_outliers(zillow_df)
    
def _remove_outliers(zillow_df):
    
    # Bathroom outliers
    q1_bath = zillow_df.bathrooms.quantile(.25)
    q3_bath = zillow_df.bathrooms.quantile(.75)
    iqr_bath = q3_bath - q1_bath

    upper_bath = q3_bath + (1.5 * iqr_bath)
    lower_bath = q1_bath - (1.5 * iqr_bath)

    # Bedroom outliers
    q1_beds = zillow_df.bedrooms.quantile(.25)
    q3_beds = zillow_df.bedrooms.quantile(.75)
    iqr_beds = q3_beds - q1_beds

    upper_beds = q3_beds + (1.5 * iqr_beds)
    lower_beds = q1_beds - (1.5 * iqr_beds)
    
    # Sqft outliers
    q1_sqft = zillow_df.total_sqft.quantile(.25)
    q3_sqft = zillow_df.total_sqft.quantile(.75)
    iqr_sqft = q3_sqft - q1_sqft

    upper_sqft = q3_sqft + (1.5 * iqr_sqft)
    lower_sqft = q1_sqft - (1.5 * iqr_sqft)
    
    # Tax value outliers
    q1_value = zillow_df.tax_value.quantile(.25)
    q3_value = zillow_df.tax_value.quantile(.75)
    iqr_value = q3_value - q1_value

    upper_value = q3_value + (1.5 * iqr_value)
    lower_value = q1_value - (1.5 * iqr_value)
    
    non_outliers = (zillow_df.bathrooms > lower_bath) & (zillow_df.bathrooms < upper_bath) & (zillow_df.bedrooms > lower_beds) & (zillow_df.bedrooms < upper_beds) & (zillow_df.total_sqft > lower_sqft) & (zillow_df.total_sqft < upper_sqft) & (zillow_df.tax_value > lower_value) & (zillow_df.tax_value < upper_value)
    
    return zillow_df[non_outliers]

def prepare_zillow(unprepared_zillow):
    prepped_data = {}
    
    prepped_data['population'] = _clean_zillow(unprepared_zillow)
    prepped_data['samples'] = split_dataframe_continuous_target(prepped_data['population'], 'tax_value')
    
    return prepped_data 