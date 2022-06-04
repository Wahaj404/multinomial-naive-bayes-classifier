from collections import defaultdict
from nltk.corpus import wordnet


def relation_list(vocab):
    relations = defaultdict(list)

    for v in vocab:
        relation = []

        def append_if_present(func):
            if len(func) > 0:
                relation.append(func[0].name().split(".")[0])

        for syn in wordnet.synsets(v, pos=wordnet.NOUN):
            for lemma in syn.lemmas():
                relation.append(lemma.name())
                append_if_present(lemma.antonyms())
            for lemma in syn.hyponyms():
                append_if_present(lemma.hyponyms())
            for lemma in syn.hypernyms():
                append_if_present(lemma.hypernyms())
        relations[v].append(relation)

    return relations


def make_chain(vocab, relations):
    chains = []
    for word in vocab:
        flag = False
        for chain in chains:
            if not flag:
                for key in list(chain):
                    if key == word and not flag:
                        chain[word] += 1
                        flag = True
                    elif key in relations[word][0] and not flag:
                        syns1 = wordnet.synsets(key, pos=wordnet.NOUN)
                        syns2 = wordnet.synsets(word, pos=wordnet.NOUN)
                        if (
                            len(syns1) > 0
                            and len(syns2) > 0
                            and syns1[0].wup_similarity(syns2[0]) >= 0.5
                        ):
                            chain[word] = 1
                            flag = True
        if not flag:
            chains.append({word: 1})
            flag = True
    return chains


def prune(chain):
    ret = []
    while len(chain) > 0:
        result = chain.pop()
        if len(result) == 1:
            for value in result.values():
                if value != 1:
                    ret.append(result)
        else:
            ret.append(result)
    return ret


def get_features(vocab):
    chains = {
        next(iter(terms.keys())): list(terms)
        for terms in prune(make_chain(vocab, relation_list(vocab)))
    }
    return set(chains.keys()), chains
