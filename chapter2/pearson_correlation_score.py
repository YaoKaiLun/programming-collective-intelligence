from critics import critics
from math import sqrt

def pearson_coefficient(prefs, person1, person2):
    similar = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            similar[item] = 1

    n = len(similar)
    if n == 0:
      return 1

    sum1 = sum([prefs[person1][item] for item in similar])
    sum2 = sum([prefs[person2][item] for item in similar])

    sum1sq = sum([pow(prefs[person1][item], 2) for item in similar])
    sum2sq = sum([pow(prefs[person2][item], 2) for item in similar])

    psum = sum([prefs[person1][item] * prefs[person2][item] for item in similar])

    den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
    if den == 0: return 0

    coefficient = (psum - (sum1 * sum2)/n)/den

    return coefficient

def get_all_pearson_coefficient(prefs, person):
    coefficient = {}
    for item in prefs:
        coefficient[item] = pearson_coefficient(prefs, item, person)
    return coefficient

coefficient = get_all_pearson_coefficient(critics, 'Toby')
for item in coefficient:
    print item, coefficient[item]