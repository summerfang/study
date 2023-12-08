### Frequency Table
### Cross Tabulation
### Contingincy Table
### Histogram
### Sturges' rule
### Standard Deviation of population
$$
\sigma = \sqrt \frac{\sum_{i=1}^{n} (x_i-\bar x)^2}{N}
$$
N repesents total number of population

### Standard Deviation of samples
$$
\sigma = \sqrt \frac{\sum_{i=1}^{n} (x_i-\bar x)^2}{N-1}
$$

N represents total number of sampels.

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


#### T-distribution

#### Poisson Distribution
$$
P(X=k) = \frac {e^{-\lambda} \lambda^k}{k!}
$$

Mathmatical expectation = mean

##### Probability mass function(PMF) vs probability density function(PDF)
PMF is for discrete data and PDF is for continuous data. PDF need to integal to get the value.

#### F-distribution

#### Corelation coefficiency

#### Corelation ratio

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

#### 