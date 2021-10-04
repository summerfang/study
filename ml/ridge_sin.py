import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

x = np.array([i*np.pi/180 for i in range(60, 300, 4)])
y = np.sin(x) + np.random.normal(0, 0.15, len(x))

data = pd.DataFrame(np.column_stack([x,y]), columns=['x','y'])
plt.plot(data['x'],data['y'],'.')
plt.show()

for i in range(2,16):
    colname = 'x_{}'.format(i)
    data[colname] = x ** i

print(data.head())


def linear_regression(data, power, models_to_plot):
    predict = ['x']

    if power >= 2:
        predict.extend('x_{}'.format(i) for i in range(2, power + 1))

    lr_model = LinearRegression(normalize=True)
    lr_model.fit(data[predict], data['y'])
    y_pred = lr_model.predict(data[predict])

    if power in models_to_plot:
        plt.subplot(models_to_plot[power])
        plt.tight_layout()
        plt.plot(data['x'], y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for power: {}'.format(power))
        plt.show()


    rss = sum((y_pred-data['y']) ** 2)
    ret = [rss]
    ret.extend([lr_model.intercept_])    
    ret.extend(lr_model.coef_)
    return ret

col = ['rss', 'intercept'] + ['coef_x_{}'.format(i) for i in range(1,16)]
ind = ['model_pow_{}'.format(i) for i in range(1,16)]

coef_matrix_simple = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1:231,3:232,6:233,9:234,12:235,15:236}

for i in range(1, 16):
    coef_matrix_simple.iloc[i-1, 0:i+2] = linear_regression(data, power=i,models_to_plot=models_to_plot)

pd.options.display.float_format = '{:,.2g}'.format
print(coef_matrix_simple)


def ridge_regression(data, predictors, alpha, models_to_plot):
    ridge_model = Ridge(alpha=alpha, normalize=True)
    ridge_model.fit(data[predictors], data['y'])
    y_pred = ridge_model.predict(data[predictors])

    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'], y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: {}'.format(alpha))
        plt.show()

    rss = sum((y_pred - data['y'])**2)
    ret = [rss]
    ret.extend([ridge_model.intercept_])
    ret.extend(ridge_model.coef_)
    return ret


predictors = ['x']
predictors.extend(['x_{}'.format(i) for i in range(2,16)])

alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]
col = ['rss', 'intercept'] + ['coef_x_{}'.format(i) for i in range(1,16)]
ind = ['alpha_{}'.format(alpha_ridge[i]) for i in range(0,10)]
coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
for i in range(10):
    coef_matrix_ridge.iloc[i,] = ridge_regression(data, predictors, alpha_ridge[i], models_to_plot)

print(coef_matrix_ridge)