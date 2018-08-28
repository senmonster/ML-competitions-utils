import pandas as pd
import os
def prepare_data(data_dir): # 处理整数型和浮点型特征
    df_mini = pd.read_csv(data_dir, index_col=0, nrows=10000).fillna(-9999)
    df_type = {}
    if 'int' in list(df_mini.dtypes):
        df_mini_int = df_mini.select_dtypes(['int'])
        df_mini_int = df_mini_int.apply(pd.to_numeric, downcast='signed')
        df_mini_int = df_mini_int.apply(pd.to_numeric, downcast='unsigned')
        dict_int = dict(zip(df_mini_int.dtypes.index, df_mini_int.dtypes.values))
        df_type.update(dict_int)
    if 'float' in list(df_mini.dtypes):
        df_mini_float = df_mini.select_dtypes(['float'])
        df_mini_float = df_mini_float.apply(pd.to_numeric, downcast='float')
        dict_float = dict(zip(df_mini_float.dtypes.index, df_mini_float.dtypes.values))
        df_type.update(dict_float)

    dtype_other = [i for i in list(df_mini.dtypes) if i not in ['float', 'int']]
    if len(dtype_other) != 0:
        df_other = df_mini.select_dtypes(dtype_other)
        dict_other = dict(zip(df_other.dtypes.index, df_other.dtypes.values))
        df_type.update(dict_other)
    #df_dtype = {**dict_int, **dict_float}

    df = pd.read_csv(data_dir, dtype=df_type)#, iterator=True)
    #print(df.info())
    #print(len(np.unique(df['Id'])))
    return df
root_dir = os.path.abspath('..')
train_x = prepare_data(os.path.join(root_dir, 'raw_data/train_x.csv'))
train_y = pd.read_csv(os.path.join(root_dir,'raw_data/train_y.csv')).apply(pd.to_numeric, downcast='signed')
train = train_x.merge(train_y, on='uid', how='left')
train.to_pickle(os.path.join(root_dir,'temp_data/train.pkl'))
print('handle train done')
train_unb_x = prepare_data(os.path.join(root_dir,'raw_data/train_unlabeled.csv'))
train_unb_x.to_pickle(os.path.join(root_dir,'temp_data/train_nolabel.pkl'))
print('handle train unlabeled done')
test_x = prepare_data(os.path.join(root_dir,'raw_data/test_x.csv'))
test_x.to_pickle(os.path.join(root_dir,'temp_data/test.pkl'))
print('handle test done')
