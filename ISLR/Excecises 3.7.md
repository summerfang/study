5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the ith fitted value takes the form
$$
\hat{y_i} = x_i \hat{\beta},
$$
where
$$
\hat{\beta}=(\sum_{i=1}^{n}x_iy_i)/(\sum_{i'=1}^{n}x_{i'}^2)
$$ 
Show that we can write
$$
\hat{y_i}=\sum_{i'=1}^{n}a_{i'}y_{i'}
$$
What is $a_{i'}$?

*Note: We interpret this result by saying that the fitted values from linear regression are* linear combinations *of the response values.*


$$
\because
\hat{\beta} = \frac{x_1y_1+x_xy_2+\dots+x_ny_n}{x_1^2+x_2^2+\dots+x_n^2}
$$