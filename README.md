# Old adage "Location, location, location" holds true, but square feet is king
This project uses Zillow data to create a regression model that predicts the tax values of single unit properties.

## Goals
1. Create a model that predicts tax values of single unit properties
2. Determine the states and counties the properties are located in
3. Determine the distribution of tax rates for each county

## Setup this project
* Dependencies
    1. [utilities.py](https://github.com/david-ryan-alviola/utilities/releases)
        * Use release 2.3.2 or greater
    2. python
    3. pandas
    4. scipy
    5. sklearn
    6. numpy
    7. matplotlib.pyplot
    8. seaborn
* Steps to recreate
    1. Clone this repository
    2. Install `utilities.py` according to the instructions
    3. Setup env.py
        * Remove the .dist extension (should result in `env.py`)
        * Fill in your user_name, password, and host
        * If you did not install `utilities.py` in your cloned repository, replace the "/path/to/utilities" string with the path to where `utilities.py` is installed
    4. Open `zillow.ipynb` and run the cells

## Key Findings
1. Isolated, total square feet is the most important driver of tax value, but there is interplay with number of bedrooms and bathrooms
2. The location matters since the FIPS county code was the second largest driver of tax value
3. Age not really a factor since it was ranked lowest by all feature selectors
4. Need to improve the model since it only has an explained variance score of 0.27

## The plan
The Kanban board used for planning is [here](https://trello.com/b/PsLwYoee).

Data will be acquired from the *zillow* database and prepared based on initial examination. Scaling will not be performed until a minimum viable product (MVP) is attained.

I want to examine these possibilities:
1. Does the tax value increase as the number of bathrooms increase?
2. Does the tax value increase as the number of bedrooms increase?
3. Does the tax value increase as the total square feet incrases?
4. Does the tax value decrease with as age increases?
5. Is there a difference between tax values based on the FIPS county?

After preparation, I intend to perform univariate exploration on the entire population and use my findings to help form any other hypotheses I would like to test. Bivariate exploration will be performed on the training sample and I should be able to see how the features I selected interact with the target. I will verify my hypotheses using statistical testing and where I can move forward with the alternate hypothesis, I will use those features in multivariate exploration. By the end of exploration, I will have identified which features I wish to use in my model.

During the modeling phase I will establish a baseline model and then use my selected features to generate a regression model for each of the different methods. I will evaluate each model based on the criteria to minimize error and compare each model's performace to the baseline. Once I have selected the best modeling method, I will adjust hyperparameters to fine tune the model and use their performance on the validation sample to select the best combination of hyperparameters. Once I have fine tuned the model, I will subject it to the training sample and evaluate the results.

If time allows, I will then go back and scale my data in the preparation phase. I should also take advantage of any discoveries to perform feature engineering and see if these new features improve my model.

Once my final model is selected, I will tidy up my notebook and python modules and begin work on the presentation.

## Data Dictionary
This is the structure of the data after preparation:
#### Target
Name | Description | Type
:---: | :---: | :---:
tax_value | The assesed value of the property for tax purposes | float
#### Features
Name | Description | Type
:---: | :---: | :---:
bathrooms | The number of bathrooms a property has | float
bedrooms | The number of bedrooms a property has | float
total_sqft | The square footage of a property | float
fips_6037 | Indicates if a property is in FIPS county 6037 (Los Angeles County)| int
fips_6059 | Indicates if a property is in FIPS county 6059 (Orange County)| int
fips_6011 | Indicates if a property is in FIPS county 6011 (Colusa County)| int
age | The difference between the current year and the year the property was built | float
#### Other data
Name | Description | Type
:---: | :---: | :---:
fips | The FIPS county code of the property. No mathematical significance. | float
tax_rate | Calculated from the tax amount divided by the tax value  | float

## Results
The polynomial model with a degree of 2 was selected as the best model:
1. Lowest RMSE values
2. Lowest difference between train RMSE and validate RMSE
3. Highest train and validate R-squared and explained variance scores

Need to improve model since explained variance score was only 0.27.

## Recommendations
1. Add more features related to size of the property
2. Add more features related to the location of the property
3. Experiment outside common regression models
4. Find ways to impute missing data in original data set