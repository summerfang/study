import pandas as pd
import scipy.stats as sp

data = ['O','X','X','M','O','M','O','N']
pd_series = pd.Series(data)
counts = pd_series.value_counts()
entropy = sp.entropy(counts,base=2)
print(entropy)