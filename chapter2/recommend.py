from critics import critics
from euclidean_distance_score import similar_distance
from pearson_correlation_score import pearson_coefficient
import operator

def calc_score(prefs, person):
    total_average_score = {}
    total_similar = {}
    scores = {}
    for other in prefs:
        if other == person: continue
        similarity = pearson_coefficient(prefs, other, person)
        for item in prefs[other]:
            if item not in prefs[person]:
                total_average_score.setdefault(item, 0)
                total_average_score[item] += similarity *  prefs[other][item]
                total_similar.setdefault(item, 0)
                total_similar[item] += similarity

    for item in total_average_score:
        scores[item] = total_average_score[item] / total_similar[item]
        print item, ':'
        print 'total_average_score:', total_average_score[item], ' total_similar:', total_similar[item], ' score:', scores[item]

    return scores


scores = calc_score(critics, 'Toby')
sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

print 'recommed to watch:'
for index, item in enumerate(sorted_scores):
    print 'Top', index + 1, ': ', item[0]



