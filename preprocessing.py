from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess(corpus):
    stops = set(stopwords.words("english"))
    lemm = WordNetLemmatizer()
    return [
        [
            [
                lemm.lemmatize(term)
                for term in map(str.lower, word_tokenize(doc))
                if term not in stops and term.isalpha()
            ],
            cls,
        ]
        for doc, cls in corpus
    ]


def reduce(corpus):
    return sorted(
        [[term, i, cls] for i, (terms, cls) in enumerate(corpus) for term in terms]
    )
