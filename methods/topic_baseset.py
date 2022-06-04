from collections import defaultdict
from nltk.corpus import wordnet as wn


def get_features(corpus, tuple):
    nouns = {x.name().split(".", 1)[0] for x in wn.all_synsets("n")}
    
    counts = defaultdict(int)
    for item in tuple:
        if item[0] in nouns:
            counts[item[0]] += 1
    counts = set(sorted(counts, key=lambda k: -counts[k])[:50])

    topic_set = {term: defaultdict(int) for term in counts}
    for doc, _ in corpus:
        for i in range(1, len(doc)):
            if doc[i] in counts:
                topic_set[doc[i]][doc[i - 1]] += 1

    features = set()
    for term in topic_set:
        features.add(term)
        features.add(sorted(topic_set[term].items(), key=lambda k: -k[1])[0][0])
    return features, {feature: [feature] for feature in features}
