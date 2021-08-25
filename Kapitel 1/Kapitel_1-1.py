from collections import Counter
from collections import defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}

# Anhand der Freundschaftspaare werden die Freunde ausfindig gemacht
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)


def number_of_friends(user):
    """Wie viele Freunde hat _user_?"""
    user_id = user["id"]
    return len(friendships[user_id])


total_connections = sum(number_of_friends(user) for user in users)  # 24
num_users = len(users)
avg_friends = total_connections/num_users  # 2.4

# Liste aus Tupeln mit Id und Freundesanzahl
number_of_friends_by_id = [
    (user["id"], number_of_friends(user)) for user in users]

# sortieren der Liste nach Freundesanzahl
number_of_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)
# print(number_of_friends_by_id)

number_of_secondary_friends = [
    (user["id"], sum(number_of_friends(users[friend_id])-1 for friend_id in friendships[user["id"]])) for user in users
]
number_of_secondary_friends.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)

# print(number_of_secondary_friends)


def foaf_ids(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]
            ]


# print(foaf_ids(users[0]))


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]  # für jeden Freund
        # die Ids der Freunde des Freundes
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id  # soll nicht die Person selbst sein
        # und nicht bereits befreundet sein
        and foaf_id not in friendships[user_id]
    )


print(friends_of_friends(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (3, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "BigData")
]


def data_scientists_who_like(target_interest):
    return [
        user_id
        # da in interest nur Tuple sind, ist user_id an Stelle 0 und interest an Stelle 1 des Tuple
        for user_id, interest in interests
        if target_interest == interest
    ]


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(
        user_id
        for interest in interests_by_user_id[user["id"]]
        for user_id in user_ids_by_interest[interest]
        if user_id != user["id"]
    )


print(most_common_interests_with(users[5]))
