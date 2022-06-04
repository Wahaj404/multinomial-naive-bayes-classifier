from collections import defaultdict


def get_features( tup):
    tf_idf = defaultdict(list)

    count = 1
    for i in range(1, len(tup)):
        if tup[i][0] == tup[i - 1][0] and tup[i][1] == tup[i - 1][1]:
            count += 1
        else:
            tf_idf[tup[i - 1][0]].append([count, tup[i][2]])
            count = 1
    tf_idf[tup[len(tup) - 1][0]].append([count, tup[len(tup) - 1][2]])

    tf_idf = sorted(
        tf_idf,
        key=lambda vec: -(sum(item[0] for item in tf_idf[vec]))
        / (len(tf_idf[vec]) + 1),
    )[:100]
    return set(tf_idf), {term: [term] for term in tf_idf}
