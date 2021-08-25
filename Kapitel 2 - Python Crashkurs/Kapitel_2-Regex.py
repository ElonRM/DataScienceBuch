import re

re_examples = [
    not re.match("a", "cat"),  # cat nicht mit a beginnt
    re.search("a", "cat"),  # cat enthält ein c
    not re.search("c", "dog"),  # dog enthält kein c
    # Aufteilen bei a oder b liefert ['c', 'r', 's']
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")  # Ziffern durch Striche ersetzen
]

assert all(re_examples), "all the regex examples should be true"
