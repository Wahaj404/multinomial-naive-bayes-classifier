from itertools import chain


def get_features(f1, c1, f2, c2, f3, c3):
    return {feature for feature in chain(f1, f2, f3)}, {
        feature: cls for feature, cls in chain(c1.items(), c2.items(), c3.items())
    }
