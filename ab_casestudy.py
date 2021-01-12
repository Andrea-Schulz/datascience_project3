import pandas as pd
import matplotlib.pyplot as plt
from calculate_statistics import p_value_invariant_ab, p_value_eval_onetailed

df = pd.read_csv('ab_casestudy/homepage-experiment-data.csv')

df.plot()

data = df['Experiment Cookies'] + df['Control Cookies']
p_exp = p_value_invariant_ab(data, df['Experiment Cookies'])
p_con = p_value_invariant_ab(data, df['Control Cookies'])

p_download = p_value_eval_onetailed(df['Control Cookies'], df['Experiment Cookies'], df['Control Downloads'], df['Experiment Downloads'])

# licenses: only account for cookies in day 1-21!
p_license = p_value_eval_onetailed(df['Control Cookies'].head(n=21), df['Experiment Cookies'].head(n=21), df['Control Licenses'], df['Experiment Licenses'])

print('done')