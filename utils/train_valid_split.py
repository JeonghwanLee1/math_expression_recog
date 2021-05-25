import pandas as pd
from functools import reduce

def split_folds(grouped, k):
    '''
    split data into class-balanced k fold
    '''
    folds = [pd.DataFrame() for _ in range(k)]
    for group in grouped:
        _, group = group
        group = group.reset_index()
        indexes = [(len(group)*(i+1)//(k)) for i in range(k)]
        start = 0
        for i,index in enumerate(indexes):
            folds[i] = folds[i].append(group.loc[start:index-1,])
            start = index
    return folds

data_path = "/opt/ml/input/train_dataset/"
gt = pd.read_csv(data_path+'gt.txt',sep=".jpg\t",header=None)
gt.columns = ["image","gt"]
level = pd.read_csv(data_path+'level.txt',sep=".jpg\t",header=None)
level.columns = ['image','level']
source = pd.read_csv(data_path+'source.txt',sep=".jpg\t",header=None)
source.columns = ['image','source']

data_frames = [gt,level,source]
df_merged = reduce(lambda left,right: pd.merge(left,right,on=['image'],how='outer'), data_frames)
df_merged


gr = []
grouped = df_merged.groupby('level')
for group in list(grouped):
    level, group = group
    group = group.groupby('source')
    gr.extend(list(group))

folds = split_folds(gr,5)
