# Twitter
Word Embedding

## Getting Started
With scraping twitter data using tweepy API, word2vec model in Gnsim is used for analogy prediction and K-means Clustering is used for word clustering in this assignment.  


### Prerequisites

Tweepy (ver.3.8) download 

```
Pip install tweepy
```

Nltk toolkit download 

```
nltk.download(words)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Data

Collected 161152 number of tweets, from 2019-11-15 to 2019-12-17
Combined 35 csv files for getting only text data.

* `dic.txt` - buit in dictionary for hashtag
* `traninig_data.txt` - scrapped twitter data
* `question-words.txt` - test data



###Usage


* `srscrappingTwitter.py` - scrapping twitter data
* `twitter_preprocessor.py` - twitter text data preprocessor
* `splithash.py` - hashtag segmentation
* `toTxt` - combine all csv files and extract text with preporcesssing 

* `NLP_taks1.ipynb` - For task1 : Analogy prediction
* `NLP_taks2.ipynb` - For task2 : K-mean clustering 

