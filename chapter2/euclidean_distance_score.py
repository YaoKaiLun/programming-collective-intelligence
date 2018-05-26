from math import sqrt

critics={
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5, 
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5, 
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0, 
        'You, Me and Dupree': 3.5}, 
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0, 
        'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    }, 
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5
    },
    'Toby': {
        'Snakes on a Plane':4.5,
        'You, Me and Dupree':1.0,
        'Superman Returns':4.0
    }
}

def similar_distance(prefs, person1, person2):
    similar = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            similar[item] = 1
            
    if len(similar) == 0: return 0
    
    total_distance = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in similar])

    average_distance = 1 + sqrt(total_distance)  # add 1 to avoid total_distace equal 0

    score = 1 / average_distance
  
    return score
    
def range_similar(prefs, person):
    scores = [(similar_distance(prefs, item, person), item) for item in prefs if item != person]
    scores.sort()
    return scores
    
for item in range_similar(critics, 'Michael Phillips'):
    print item
