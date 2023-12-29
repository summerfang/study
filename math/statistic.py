import statsmodels.api as sm

ci = sm.stats.proportion_confint(649 * 0.85, 649, alpha=0.05, method='normal')
print(ci)