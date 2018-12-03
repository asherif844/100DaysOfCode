file = '/Users/asherif844/OneDrive - Microsoft/schema.txt'
odd = []
even = []
odd2 = []
with open(file, 'r') as fin:
    for count, line in enumerate(fin, start=1):
        if count %2 == 0:
            line = line.strip('\n')
            line = line+','
            even.append(line)
        else:
            line = line.strip('\n')
            odd.append(line)
# generate matrix with 299 columns and 1 million rows
import numpy as np
import pandas as pd
import pickle

df = pd.DataFrame(even, odd)
# df['even2'] = df['even']+str("',")
# print(df)

# print(len(odd), len(even))
# df.to_csv('schema.csv', sep = ' ')
# a = np.random.rand(299,1000000)
# print(a.shape)
lst = df.iloc[:, 0:0]
# lst.to_csv('file.csv')

# with open('lists.txt', 'w' ) as ls:
#     pickle.dump(lst, ls)
        
# print(lst)

# with open('lists2.txt', 'w') as columns:
#     for i in lst:
#         columns.write(i)+'\n'

# fo = open('lists.txt', 'w')
# line = fo.write(str(lst))
# fo.close()

print(odd)