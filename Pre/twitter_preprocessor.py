import string
import nltk
from nltk.corpus import stopwords
from nltk import re
from splithash import segment

MIN_YEAR = 1900
MAX_YEAR = 2100

def get_url_patern():
    return re.compile(
        r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))'
        r'[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})')


def get_emojis_pattern():
    #emojis_pattern= re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u26FF\u2700-\u27BF]+',re.UNICODE)

    emojis_pattern = re.compile("["
               u"\U0001F600-\U0001F64F"  # emoticons
               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
               u"\U0001F680-\U0001F6FF"  # transport & map symbols
               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
               u"\U00002500-\U00002BEF"  # chinese char
              u"\U00002702-\U000027B0"
              u"\U00002702-\U000027B0"
             u"\U000024C2-\U0001F251"
             u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"  # dingbats
                u"\u3030"
                "]+", re.UNICODE)

    return emojis_pattern


def get_hashtags_pattern():
    return re.compile(r'#([^\s]+)')

def compound_word_split(self, compound_word):
    """
    Split a given compound word(string) and return list of words in given compound_word
    Ex: compound_word='pyTWEETCleaner' --> ['py', 'TWEET', 'Cleaner']
    """
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', compound_word)
    return [m.group(0) for m in matches]


def get_single_letter_words_pattern():
    return re.compile(r'(?<![\w\-])\w(?![\w\-])')


def get_blank_spaces_pattern():
    return re.compile(r'\s{2,}|\t')


def get_twitter_reserved_words_pattern():
    return re.compile(r'(RT|rt|FAV|fav|VIA|via)')


def get_mentions_pattern():
    return re.compile(r'@\w*')

def get_arabic_pattern():
    #return re.compile('[\u0627-\u064a]')
    return re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+' )
def get_negations_pattern():

    negations_ = {"isn't": "is not", "can't": "can not", "couldn't": "could not", "hasn't": "has not",
                  "hadn't": "had not", "won't": "will not", "dont":'do not',"isnt":"is not",
                  "wouldn't": "would not", "aren't": "are not",
                  "haven't": "have not", "doesn't": "does not", "didn't": "did not",
                  "don't": "do not", "shouldn't": "should not", "wasn't": "was not", "weren't": "were not",
                  "mightn't": "might not",
                  "mustn't": "must not"}
    return re.compile(r'\b(' + '|'.join(negations_.keys()) + r')\b')


def is_year(text):
    if (len(text) == 3 or len(text) == 4) and (MIN_YEAR < len(text) < MAX_YEAR):
        return True
    else:
        return False


class TwitterPreprocessor:

    def __init__(self, text: str):
        self.text = text

    def fully_preprocess(self):
        return self \
            .remove_emoji()\
            .remove_urls() \
            .remove_mentions() \
            .remove_hash2() \
            .remove_twitter_reserved_words() \
            .remove_punctuation() \
            .remove_arabic()\
            .remove_single_letter_words() \
            .remove_blank_spaces() \
            .remove_stopwords() \
            .remove_numbers()

    # .remove_hashtags() \

    def remove_emoji(self):
        self.text = re.sub(pattern= get_emojis_pattern(), repl='', string=self.text)
        return self


    def remove_urls(self):
        self.text = re.sub(pattern=get_url_patern(), repl='', string=self.text)
        return self

    def remove_punctuation(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self

    def remove_mentions(self):
        self.text = re.sub(pattern=get_mentions_pattern(), repl='', string=self.text)
        return self

    def remove_hashtags(self):
        self.text = re.sub(pattern=get_hashtags_pattern(), repl=r'\1', string=self.text) #left word delete only hash tag
        #self.text = re.sub(pattern=get_hashtags_pattern(), repl=segement(r'\1'), string=self.text) #left word delete only hash tag
        # text = re.sub(r'#([^\s]+)', r'\1', text)
        #self.text = re.sub(pattern=get_hashtags_pattern(), repl='', string=self.text) #completely delete hashtag

        return self
    def remove_arabic(self):
        self.text=re.sub(pattern=get_arabic_pattern(),repl='',string=self.text) #araibc
        return self

    def remove_twitter_reserved_words(self):
        self.text = re.sub(pattern=get_twitter_reserved_words_pattern(), repl='', string=self.text)
        return self

    def remove_single_letter_words(self):
        self.text = re.sub(pattern=get_single_letter_words_pattern(), repl='', string=self.text)
        return self

    def remove_blank_spaces(self):
        self.text = re.sub(pattern=get_blank_spaces_pattern(), repl=' ', string=self.text)
        return self

    def remove_stopwords(self, extra_stopwords=None):
        if extra_stopwords is None:
            extra_stopwords = []
        text = nltk.word_tokenize(self.text)

        stop_words = set(stopwords.words('english'))

        new_sentence = []
        for w in text:
            if w not in stop_words and w not in extra_stopwords:
                new_sentence.append(w)
        self.text = ' '.join(new_sentence)
        return self

    def remove_hash2(self):
        self.text = segment(self.text)
        return self

    def remove_numbers(self, preserve_years=False):
        text_list = self.text.split(' ')
        for text in text_list:
            if text.isnumeric():
                if preserve_years:
                    if not is_year(text):
                        text_list.remove(text)
                else:
                    text_list.remove(text)

        self.text = ' '.join(text_list)
        return self

    def lowercase(self):
        self.text = self.text.lower()
        return self
    
    def handle_negations(self):  
        self.text = re.sub(pattern=get_negations_pattern(), repl='', string=self.text)
        return self
