from collections import defaultdict


empty_dict = {}
empty_dict_2 = dict()  # nicht üblich
grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("Kate has no grade")

joel_has_grade = "Joel" in grades  # True
kate_has_grade = "Kate" in grades  # False

joels_grade = grades.get("Joel", 0)  # 80
kates_grade = grades.get("Kate", 0)  # 0
no_ones_grade = grades.get("No one")  # der Standardwert ist None

grades["Tim"] = 99
grades["Kate"] = 100  # fügt einen Eintrag für Kate automatisch hinzu
num_students = len(grades)

tweet = {
    "user": "joelgrus",
    "text": "Data Scienceis awesome",
    "rewtweet count": 100,
    "hashtags": ["#data", "#science", "datascience", "awesome", "yolo"]
}

tweet_keys = tweet.keys()  # Iterable für die keys
tweet_values = tweet.values()  # Iterable für die Wete
tweet_items = tweet.items()  # Iterable für die (Schlüssel,Wert)-Tupels

"user" in tweet_keys  # True aber nicht üblich
"user" in tweet  # True und üblich in Python

"joelgrus" in tweet_values  # True und der einzige Weg, dies zu testen


# DEFAULTDICT

document = "huhu ich verkaufe dich"

word_counts = {}
for word in document:
    word_count = word_counts.get(word, 0)
    word_counts[word] = word_count+1

# Lösung mithilfe eines defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)  # nun ist dd_list  {2: [1]}
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"  # {"Joel": {"City": "Seattle}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1  # nun enthält dd_pair {2:[0, 1]}
