import pandas as pd
from pandas.core.algorithms import SelectNSeries
from pandas.core.dtypes.missing import isna
from scipy.sparse import data

card_tab = pd.read_csv('./card_tab.csv')
start_train = pd.read_csv('./start_train.csv')
start_test = pd.read_csv('./start_test.csv')

print(len(card_tab))
print(len(start_train))
print(len(start_test))

card_tab = card_tab.drop_duplicates(subset=['id'], keep=False)
print(len(card_tab))

start_train = start_train.drop_duplicates(['id'], keep=False)
print(len(start_train))

start_test = start_test.drop_duplicates(['id'], keep=False)
print(len(start_test))

train = pd.merge(start_train, card_tab, on=['id'], how='left')
print(len(train))
test = pd.merge(start_test, card_tab, on=['id'], how ='left')
print(len(test))

print(train['types'].describe())
print(test['types'].describe())

print("\n")

print(train['toughness'].value_counts())
print("\n")
print(train.groupby(['toughness']).size())

def rarity2num(rarity_name):
    if rarity_name == 'Common':
        return 1
    if rarity_name == 'Uncommon':
        return 2
    if rarity_name == 'Rare':
        return 3
    if rarity_name == 'Mythical':
        return 4
    
    return 0

train['rarity_num'] = train.apply(lambda x : rarity2num(x['rarity']), axis=1)
test['rarity_num'] = test.apply(lambda x : rarity2num(x['rarity']), axis=1)

def toughness2num(toughness):
    if toughness == "*" or isna(toughness):
        return 0
    else:
        return int(toughness)

train['toughness_num'] = train.apply(lambda x: toughness2num(x['toughness']), axis=1)
test['toughness_num'] = test.apply(lambda x: toughness2num(x['toughness']), axis=1)

def power2num(power):
    if power == '*' or isna(power) or power == '1+*':
        return 0
    else:
        return int(power)

train['power_num'] = train.apply(lambda x: power2num(x['power']), axis=1)
test['power_num'] = test.apply(lambda x: power2num(x['power']), axis=1)

train_1 = train[['future_price','cmc','toughness_num','power_num','rarity','types']]
print(train_1.head())
train_1 = train.dropna(subset=['future_price','cmc','toughness_num','power_num','rarity','types'],inplace=True)

print(train_1.head(10))
print(test.head(10))

train = train.dropna(inplace=True)

print(train.shape)
print(train.describe())
print(train.dtypes)

#import seaborn as sns
# sns.pairplot(train, hue='types')

# print(train.corr())
# sns.heatmap(train.corr(), annot=True, lw=1)

# sns.boxplot(y='future_price',x='rarity', data=train)
# sns.boxplot(y='future_price',x='toughness', data=train)
# sns.boxplot(y='future_price',x='power', data=train)
# sns.boxplot(y='future_price',x='types', data=train)
# sns.boxplot(y='future_price',x='colors', data=train)

# Dummy

X = train[['cmc','toughness_num','power_num','rarity','types']]
X = pd.get_dummies(data=X, drop_first=True)

Y = train['future_price']

print(train['cmc'].value_counts())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=101)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

print(lr.intercept_)
print(lr.coef_)


pred_y = lr.predict(test['cmc'])
print(pred_y)

from sklearn import metrics
