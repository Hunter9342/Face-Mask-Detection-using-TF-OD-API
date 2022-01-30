import numpy as np
import os
import pandas as pd
np.random.seed(1)

label_path=os.path.join(os.getcwd(),'data\mask_labels.csv')
full_labels = pd.read_csv(label_path)


grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()

gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]
len(grouped_list)

train_index = np.random.choice(len(grouped_list), size=753, replace=False)
test_index = np.setdiff1d(list(range(853)), train_index)

#print(len(train_index),len(test_index))

train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])

#print(len(train), len(test))

train.to_csv('data/train_labels.csv', index=None)
test.to_csv('data/test_labels.csv', index=None)


