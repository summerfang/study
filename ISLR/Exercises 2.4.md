
1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.
    
    (a) The sample size n is extremely large, and the number of predictors p is small.<br>
    (b) The number of predictors p is extremely large, and the number of observations n is small.<br>
    (c) The relationship between the predictors and response is highly non-linear.<br>
    (d) The variance of the error terms, i.e. σ2 = Var(ǫ), is extremely high.

2. Explain whether each scenario is a classification or regression problem,
and indicate whether we are most interested in inference or prediction.
Finally, provide n and p.

    (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.<br>
    (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.<br>
    (c) We are interest in predicting the ed % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the

3. We now revisit the bias-variance decomposition.

    (a) Provide a sketch of typical (squared) bias, variance, training error,test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less flexible statistical learning methods towards more flexible approaches. The x-axis should represent the amount of flexibility in the method, and the y-axis should represent the values for each curve. There should be five curves. Make sure to label each one.<br>
    (b) Explain why each of the five curves has the shape displayed in part (a).

4. You will now think of some real-life applications for statistical learning.

    (a) Describe three real-life applications in which classification might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.<br>
    (b) Describe three real-life applications in which regression might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.<br>
    (c) Describe three real-life applications in which cluster analysis might be useful.

5. What are the advantages and disadvantages of a very flexible (versus
a less flexible) approach for regression or classification? Under what
circumstances might a more flexible approach be preferred to a less
flexible approach? When might a less flexible approach be preferred?

6. Describe the differences between a parametric and a non-parametric
statistical learning approach. What are the advantages of a parametric
approach to regression or classification (as opposed to a nonparametric
approach)? What are its disadvantages?

7. The table below provides a training data set containing six observations,
three predictors, and one qualitative response variable.

    |Obs.|X1| X2| X3|    Y|
    |----|--|---|---|-----|
    |1   | 0|  3|  0|  Red|
    |2   | 2|  0|  0|  Red|
    |3   | 0|  1|   |  Red|
    |4   | 0|  1|  2|Green|
    |5   |−1|  0|  1|Green|
    |6   | 1|  1|  1|  Red|

    Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.<br>

    (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0 <br>
    (b) What is our prediction with K = 1? Why?<br>
    (c) What is our prediction with K = 3? Why?<br>
    (d) If the Bayes decision boundary in this problem is highly nonlinear,then would we expect the best value for K to be large or small? Why?