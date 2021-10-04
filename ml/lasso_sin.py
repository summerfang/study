import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

x = np.array([i*np.pi/180 for i in range(60, 300, 4)])
y = np.sin(x) + np.random.normal(0, 0.15, len(x))

data = pd.DataFrame(np.column_stack([x,y]), columns=['x','y'])
plt.plot(data['x'],data['y'],'.')
plt.show()

for i in range(2,16):
    colname = 'x_{}'.format(i)
    data[colname] = x ** i

def lasso_regression(data, predictors, alpha, models_to_plot={}):
    lasso_model = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    lasso_model.fit(data[predictors], data['y'])
    y_pred = lasso_model.predict(data[predictors])

    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'], y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: {}'.format(alpha))
        plt.show()

    rss = sum((y_pred - data['y'])**2)
    ret = [rss]
    ret.extend([lasso_model.intercept_])
    ret.extend(lasso_model.coef_)
    return ret


predictors = ['x']
predictors.extend(['x_{}'.format(i) for i in range(2,16)])

alpha_lasso = [1e-15, 1e-10, 1e-8, 1e-5,1e-4, 1e-3,1e-2, 1, 5, 10]
col = ['rss', 'intercept'] + ['coef_x_{}'.format(i) for i in range(1,16)]
ind = ['alpha_{}'.format(alpha_lasso[i]) for i in range(0,10)]
coef_matrix_lasso = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1e-10:231, 1e-5:232,1e-4:233, 1e-3:234, 1e-2:235, 1:236}
for i in range(10):
    coef_matrix_lasso.iloc[i,] = lasso_regression(data, predictors, alpha_lasso[i], models_to_plot)

print(coef_matrix_lasso)