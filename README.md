# regression-project
This project uses Zillow data to create a regression model that predicts the tax values of single unit properties.

## Goals
1. Create a model that predicts tax values of single unit properties
2. Determine the states and counties the properties are located in
3. Determine the distribution of tax rates for each county

## Setup this project

## Key Findings

## The plan
The Kanban board used for planning is [here](https://trello.com/b/PsLwYoee).

Data will be acquired from the *zillow* database and prepared based on initial examination. Scaling will not be performed until a minimum viable product (MVP) is attained.

After preparation, I intend to perform univariate exploration on the entire population and use my findings to help form any other hypotheses I would like to test. Bivariate exploration will be performed on the training sample and I should be able to see how the features I selected interact with the target. I will verify my hypotheses using statistical testing and where I can move forward with the alternate hypothesis, I will use those features in multivariate exploration. By the end of exploration, I will have identified which features I wish to use in my model.

During the modeling phase I will establish a baseline model and then use my selected features to generate a regression model for each of the different methods. I will evaluate each model based on the criteria to minimize error and compare each model's performace to the baseline. Once I have selected the best modeling method, I will adjust hyperparameters to fine tune the model and use their performance on the validation sample to select the best combination of hyperparameters. Once I have fine tuned the model, I will subject it to the training sample and evaluate the results.

If time allows, I will then go back and scale my data in the preparation phase. I should also take advantage of any discoveries to perform feature engineering and see if these new features improve my model.

Once my final model is selected, I will tidy up my notebook and python modules and begin work on the presentation.
