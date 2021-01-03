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



### Usage

Data Preprocessing
* `srscrappingTwitter.py` - scrapping twitter data
* `twitter_preprocessor.py` - twitter text data preprocessor
* `splithash.py` - hashtag segmentation
* `toTxt` - combine all csv files and extract text with preporcesssing 

Task
* `NLP_taks1.ipynb` - For task1 : Analogy prediction
* `NLP_taks2.ipynb` - For task2 : K-mean clustering 


### Data Set and Preprocessing
By using tweeps API,  61152 number of tweets are collected. The data has collected from 2019-11-15 to 2019-12-17. the specific keyword that helps to collect the data related to the test dataset containing the word about the capital city, currency family relationship.


* Remove emoji
* Remove URL
* Remove mentions
* Remove hashtag and segment
* Remove reserved word
* Remove other language except English • Remove stopwords and punctuation
* Remove single word
* Remove number and blank


### Task 1 : Analogy Prediction

The word2vec model which is based on neural network layers is used to embed the words. Words are represented as vectors. The underlying assumption of the word2vec model is that words that share the same context also shares the same semantic meaning. In this task, open-sourced Gensim python library is used to train the model as it is easy to implement.



### Task 2 : Word Clustering


Word clustering is a unsupervised learning technique for partitioning set of words into subsets of semantically similar words. There are four types clustering algorithms. Connectivity, centroid, density and distribution. The main difference between these algorithms is the distance of the data points in the data space. The cenrtoid algorithm, specifically K-means is made use of to obtain the word clusters.

### References
* GitHub : Twitter Tweepy ( https://github.com/tweepy/tweepy )
* GitHub : Hashtag segment ( https://github.com/jchook/wordseg )
* Wiki : Viterbi algorithm ( https://en.wikipedia.org/wiki/Viterbi_algorithm )
* Gensim word2vec ( https://radimrehurek.com/gensim/models/word2vec.html )
* Topic Modeling ( https://monkeylearn.com/topic-analysis/ ) 
