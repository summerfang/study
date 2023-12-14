### Frequency Table
### Cross Tabulation
### Contingincy Table
### Histogram
### Sturges' rule

### These terminology is for x
### Standard Deviation of population
$$
\sigma = \sqrt \frac{\sum_{i=1}^{n} (x_i-\bar x)^2}{N}
$$
N repesents total number of population

### Variance
$$
\sigma ^2 = \sum (x-\bar x)^2
$$

### Standard Deviation of samples
$$
\sigma = \sqrt \frac{\sum_{i=1}^{n} (x_i-\bar x)^2}{N-1}
$$

### Standard error
$$
SE = \frac {\sigma} {\sqrt n}
$$

N represents total number of sampels.

### These teminologies are related with y
### What is $R^2$

$$
R^2 = 1 - \frac {RSS}{TSS} \\
RSS = \sum (y-f(x_i))^2 \\
TSS = \sum (y_i-\bar y)^2
$$

### What is MSE and RMSE
$$
MSE = \frac {\sum (y_i-\hat y)^2}{n} \\

and \\

RMSE = \sqrt {MSE}
$$

### Standard score
### z-score
z-score $ = \frac{x_i-\bar{x}}{\sigma}$ which is used to search Z-score table

### Probability density function
### Deagree of freedom
#### Normal Distribution
$$
f(x) = \frac{1}{\sigma \sqrt {2 \pi}} e^{-\frac {1}{2}(\frac {x-\bar x}{\sigma})^2}
$$

#### Degree of freedom (df)



####  Chi-Square Distribution
$$
\begin{aligned}
f(\chi) &= \frac {1}{2^{\frac{df}{2} \times \int_{0}^{\infin} \chi ^ {\frac {df}{2}-1}}e^{-\chi}d\chi} \times \chi^{\frac{df}{2}-1} \times e^{-\frac{\chi}{2}} \,, &\chi>0\\

f(\chi) &= 0, \ &\chi \le 0 
\end{aligned}
$$ 

[Normal Distribution Table](https://www.mathsisfun.com/data/standard-normal-distribution-table.html)  vs [Z-score table](https://www.z-table.com/)

They are diffferent.



#### Poisson Distribution
$$
P(X=k) = \frac {e^{-\lambda} \lambda^k}{k!}
$$

#### Mathmatical expectation = mean

##### Probability mass function(PMF) vs probability density function(PDF)
PMF is for discrete data and PDF is for continuous data. PDF need to integal to get the value.

#### T-distribution

#### F-distribution
The F-distribution is used to compare whether two populations are belong to same variable. If their covariance is same, they are belong to the same variable and te F statistic will be close to 1. Or it will be greater than 1.

#### Corelation coefficiency
$$
\frac {\sum(x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2}\sqrt {\sum(y-\bar{y})^2}} = \frac {S_{xy}}{S_{xx}S_{yy}}
$$

#### Covariance
$$
cov(x,y) = \frac {\sum(x-\bar x)(y-\bar y)}{N} \  \text{covariance for population} \\
cov(x,y) = \frac {\sum (x-\bar x)(y - \bar y)}{N-1} \ \text{covariance for sample} \\

Corelation \ coefficien = \frac {cov(x,y)}{\sigma_x \sigma_y} \\
\sigma_x = \sqrt {\frac {\sum (x- \bar x)^2}{N}} \\
\sigma_y = \sqrt {\frac {\sum (y- \bar y)^2}{N}} \\
\sigma_x \sigma_y = \frac {\sqrt {\sum (x-\bar x)^2} \sqrt{\sum (y-\bar y)^2}}{N} \\
Corelation \ coefficien = \frac {\sum(x-\bar x)(y-\bar y)}{N} * \frac {N}{\sqrt {\sum (x-\bar x)^2} \sqrt{\sum (y-\bar y)^2}} \\= \frac {\sum(x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2}\sqrt {\sum(y-\bar{y})^2}} \ \text {Same as above}

$$



#### Corelation ratio
$$
\frac {interclass \ variance}{interclass \ variance + intraclass \ variance}
$$

#### Cramers' coefficient
It is used to measure the relation between two categorical variables. It is also named as Cramer's V or $\varphi$



The book has a mistake about the last step to calculate from $\Chi^2$ to Cramer's V. 

The book says to calcualte Cramer's coefficient, it is:
$$
\sqrt \frac {\Chi^2}{\text {the total number of values} \times \text {the min of } (\text {the total number of lines in the cross tabulation - 1}, \text{the number of rows in the cross tabulation - 1})}
$$

It should be the column and row not line and row.

This is better formula about Cramer's V:
$$
V = \sqrt {\frac {\Chi^2}{n \times min(k-1, r-1)}}
$$

#### Comparasion method

* Numerical vs Categorical
* One variable vs Two variables
    - mean, median, min, max, mode, count
    - variance, standard deviation, standard error
    - covariance, covariance matrix
* Numerical vs Numerical
* Numerical vs Categorical
* Categorical vs Categorical
* z test
* t test
* f test
* chi-squared $\chi^2$ test
