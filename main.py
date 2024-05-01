import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
data['human'] = data.apply(lambda row:  1 if row['whoAmI'] == 'human' else 0, axis=1)
data['robot'] = data.apply(lambda row:  1 if row['whoAmI'] == 'robot' else 0, axis=1)
print(data)