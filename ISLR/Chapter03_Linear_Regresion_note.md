## 1. The calculus process for estimate $\beta_0,\beta_1$

### How to estimate $\beta_0$: 

Know as  
$$
RSS = \sum (y_i-\hat{y_i})^2 \\
\because
\hat{y_i} = \beta_0+\beta_1x_i\\
RSS = \sum (y_i-\beta_0-\beta_1x_i)^2
$$
To minimize RSS, it mean minimize RSS to zero since it is squared.
Let's do partial derivative on $\beta_0$
$$
\frac{\partial RSS}{\partial \beta_0}=\frac{\partial \sum (y_i-\beta_0-\beta_1x_i)^2}{\partial \beta_0}
$$
According to composite function derivative rule (Chain rule):
$$
f'(g(x)) = f'(u=g(x))\times g'(x)
$$
Assume $u=y_i-\beta_0-\beta_1x_i$
$$
\frac{\partial RSS}{\partial \beta_0}=\frac{d\sum u^2}{d\beta_0} \times \frac{du}{d\beta_0} \\
= 2 \times (\sum u) \times (y_i-\beta_0-\beta_1x_i)'\\
= 2 \times (\sum  (y_i-\beta_0-\beta_1x_i)) \times (-1) \\
= -2 \times \sum   (y_i -(\beta_0+\beta_1x_i)) \\
= -2 \times ((n \times \bar{y}) -  n \times (\beta_0 +  \beta_1 \times \bar{x})) \\ = 0 \\
$$

So
$$
n \times \bar{y} = n \times (\beta_0 +  \beta_1 \times \bar{x}) \\
\bar{y} = \beta_0 +\beta_1 \times \bar{x} \\
$$
$$
\begin{equation}
\beta_0 = \bar{y}-\beta_1 \bar{x} \\
\end{equation}
$$

### How to estimate $\beta_1$
Know as  
$$
RSS = \sum (y_i-\hat{y_i})^2 \\
\because
\hat{y_i} = \beta_0+\beta_1x_i\\
RSS = \sum (y_i-\beta_0-\beta_1x_i)^2
$$
To minimize RSS, it mean minimize RSS to zero since it is squared.
Let's do partial derivative on $\beta_1$
$$
\frac{\partial RSS}{\partial \beta_0}=\frac{\partial \sum (y_i-\beta_0-\beta_1x_i)^2}{\partial \beta_1}
$$
According to composite function derivative rule (Chain rule):
$$
f'(g(x)) = f'(u=g(x))\times g'(x)
$$
Assume $u=y_i-\beta_0-\beta_1x_i$
$$
\frac{\partial RSS}{\partial \beta_1}=\frac{d\sum u^2}{d\beta_1} \times \frac{du}{d\beta_1} \\
= 2 \times (\sum u) \times (y_i-\beta_0-\beta_1x_i)'\\
= 2 \times (\sum  (y_i-\beta_0-\beta_1x_i)) \times (-x_i) \\
= -2 \times (\sum  (x_iy_i-\beta_0x_i-\beta_1x_i^2)) \\
$$

So
$$
\sum  (x_iy_i-\beta_0x_i-\beta_1x_i^2) = 0 \\
\sum x_iy_i-\sum \beta_0x_i - \sum \beta_1x^2 = 0 \\
\sum x_iy_i-\sum \beta_0x_i = \sum \beta_1x^2 \\

$$

According to estimation of $\beta_0$
$$
\beta_0 = \bar{y}-\beta_1 \bar{x}
$$
So:
$$
\begin{aligned}
\sum x_iy_i - \sum x_i  (\bar{y}-\beta_1 \bar{x}) &= \beta_1\sum x_i^2 \\ 
\sum x_iy_i - \sum x_i \bar{y} + \beta_1\sum  x_i\bar{x} &= \beta_1\sum x_i^2 \\ 
\beta_1 &=\frac {\sum x_iy_i - \sum x_i \bar{y} }{\sum x_i^2 - \sum x_i\bar{x}} \\
\end{aligned}
$$
So, we have
$$
\begin{equation}
\beta_1 =\frac {\sum x_i(y_i -\bar{y}) }{\sum x_i(x_i - \bar{x})} 
\end{equation}
$$

$$
\begin{aligned}
\because
\sum(y_i - \bar{y}) = \sum y_i -n \times \bar{y} &= \sum(x_i-\bar{x}) = \sum x_i -n \times \bar{x} = 0 , \\
\beta_1 &=\frac {\sum x_i(y_i -\bar{y}) - \sum \bar{x}(y_i - \bar{y})  }{\sum x_i(x_i - \bar{x})-\sum \bar{x}(x_i-\bar{x})} \\
\end{aligned}
$$
Finally, we have
$$
\begin{equation}
\beta_1 =\frac {\sum (x_i - \bar{x})(y_i -\bar{y})}{\sum (x_i - \bar{x})^2} \\
\end{equation}
$$


### 2. [This is a best video to explain how to estimate $\beta_0, and \ \beta_1$](https://www.youtube.com/watch?v=ewnc1cXJmGA)

