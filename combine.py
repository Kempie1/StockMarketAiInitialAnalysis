import pandas as pd


df1 = pd.read_csv('data/20to21.csv')
df2 = pd.read_csv('data/19to20.csv')
df3 = pd.read_csv('data/18to19.csv')
df4 = pd.read_csv('data/17to18.csv')
df5 = pd.read_csv('data/16to17.csv')
df6 = pd.read_csv('data/15to16.csv')
df7 = pd.read_csv('data/14to15.csv')
df8 = pd.read_csv('data/13to14.csv')
df9 = pd.read_csv('data/12to13.csv')
df10 = pd.read_csv('data/11to12.csv')
df11 = pd.read_csv('data/10to11.csv')
df12 = pd.read_csv('data/9to10.csv')
df13 = pd.read_csv('data/8to9.csv')
df14 = pd.read_csv('data/7to8.csv')
df15 = pd.read_csv('data/6to7.csv')
df16 = pd.read_csv('data/5to6.csv')
frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16]
result = pd.concat(frames)
compression_opts = dict(method='zip',
                        archive_name='5to21.csv')  
result.to_csv('out.zip', index=False,
          compression=compression_opts)