import env
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from utilities import evaluate_hypothesis_pcorrelation, evaluate_hypothesis_ttest

def explore_bivariate_categorical(target, cat_vars, train):
    
    for var in cat_vars:
        _print_header(var, target)
        
        sns.boxplot(x=var, y=target, data=train)
        plt.show()
        
        print()
        
        sns.barplot(x=var, y=target, data=train)
        plt.show()
        
        print("-------------------------------")
        print(f"Mean {target} by {var}:  ")
        print(train.groupby(var)[target].mean())
        print()
        
def explore_bivariate_continuous(target, cont_vars, train):
    
    for var in cont_vars:
        _print_header(var, target)
        
        sns.relplot(x=var, y=target, data=train)
        plt.show()
        corr, p = stats.pearsonr(train[var], train[target])
        
        print("-------------------------------")
        print(f"Correlation between {var} and {target}:  {corr}")
        print(f"P value:  {p}")
        print()
        
def explore_multivariate(cont_vars, cat_vars, target, train):
    for cont_var in cont_vars:
        _print_header(cont_var, target)
        
        for cat_var in cat_vars:
            sns.relplot(x=cont_var, y=target, hue=cat_var, data=train)
            plt.title(f"By {cat_var}")
            plt.show()
            print()
        
def _print_header(var, target):
    print(f"{var} vs {target}")
    print("-------------------------------")
    
def test_hypothesis_correlation(var, target, train, null_hyp, alt_hyp, alpha=.05):
    corr, p = stats.pearsonr(train[var], train[target])
    evaluate_hypothesis_pcorrelation(corr, p, alpha, null_hyp, alt_hyp)
    
def test_hypothesis_ttest(target, sample, population, null_hyp, alt_hyp, alpha=.05):
    t, p = stats.ttest_1samp(sample[target], population[target].mean())
    evaluate_hypothesis_ttest(p, t, alpha, tails="greater", null_hypothesis=null_hyp, alternative_hypothesis=alt_hyp)
    
def plot_distributions(counties, x_value, group_key):
    
    for county in counties:
        sns.distplot(county[x_value])
        plt.title(county[group_key].unique())
        plt.show()
        print()
        print(county[x_value].describe())
        print("------------------------")