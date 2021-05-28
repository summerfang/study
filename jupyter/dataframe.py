import pandas as pd

score_dict = {"name":["John","Henry","James","Mary"], "Score":[90,88,76,99]}

print(score_dict)

print("-------------------")
score_df = pd.DataFrame(score_dict)

print(score_df)
