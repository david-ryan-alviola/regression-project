import env
import pandas as pd

from utilities import split_dataframe_continuous_target
from datetime import date

def _clean_zillow(df):
    zillow_df = df.copy()
    
    zillow_df = _encode_categoricals(zillow_df)
    
    zillow_df = zillow_df.rename(columns={'bathroomcnt' : 'bathrooms', 'bedroomcnt' : 'bedrooms', 'calculatedfinishedsquarefeet' : 'total_sqft', 'taxvaluedollarcnt' : 'tax_value', 'taxamount' : 'tax_amount', 6037.0 : 'fips_6037', 6059.0 : 'fips_6059', 6111 : 'fips_6111'})
    
    return _remove_outliers(_add_features(zillow_df))

def _encode_categoricals(zillow_df):
    encoded_df = zillow_df.copy()
    
    fips_dummies = pd.get_dummies(encoded_df.fips, dummy_na=False, drop_first=False)
    
    return pd.concat([encoded_df, fips_dummies], axis=1)

def _add_features(zillow_df):
    df = zillow_df.copy()
    
    df['age'] = date.today().year - df.yearbuilt
    df['tax_rate'] = df.tax_amount / df.tax_value
    df = df.drop(columns=['yearbuilt', 'tax_amount'])
    
    return df
    
def _remove_outliers(zillow_df):
    
    # Bathroom outliers
    upper_bath, lower_bath = _generate_outlier_bounds(zillow_df, 'bathrooms')

    # Bedroom outliers
    upper_beds, lower_beds = _generate_outlier_bounds(zillow_df, 'bedrooms')
    
    # Sqft outliers
    upper_sqft, lower_sqft = _generate_outlier_bounds(zillow_df, 'total_sqft')
    
    # Tax value outliers
    upper_value, lower_value = _generate_outlier_bounds(zillow_df, 'tax_value')
    
    # Age outliers
    upper_age, lower_age = _generate_outlier_bounds(zillow_df, 'age')
    
    # Tax rate outliers
    upper_rate, lower_rate = _generate_outlier_bounds(zillow_df, 'tax_rate')
    
    non_outliers = (zillow_df.bathrooms > lower_bath) & (zillow_df.bathrooms < upper_bath) & (zillow_df.bedrooms > lower_beds) & (zillow_df.bedrooms < upper_beds) & (zillow_df.total_sqft > lower_sqft) & (zillow_df.total_sqft < upper_sqft) & (zillow_df.tax_value > lower_value) & (zillow_df.tax_value < upper_value) & (zillow_df.age > lower_age) & (zillow_df.age < upper_age) & (zillow_df.tax_rate > lower_rate) & (zillow_df.tax_rate < upper_rate)
    
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