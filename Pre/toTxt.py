import glob
import pandas as pd
import os.path
from twitter_preprocessor import TwitterPreprocessor

os.chdir("/Users/seoyoung/Desktop/6000H/data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
print("finish merging csv files")

df= pd.read_csv("combined_csv.csv")


print("total number of twitter :", len(df))
txt=[]

for tweet in df.text:
    try:
        t = tweet
        p = TwitterPreprocessor(t)
        p.fully_preprocess()

        txt.append(p.text)
    except:
        print("skip blank")

with open('training_data.txt', 'w') as f:
    for item in txt:
        f.write("%s\n" % item)

print("finish preprocessing text data (train_data.txt)")
