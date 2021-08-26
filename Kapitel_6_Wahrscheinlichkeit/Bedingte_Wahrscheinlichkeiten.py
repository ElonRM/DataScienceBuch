import enum, random

# Ein Enum ist ein typisiertes Set enumerierter Werte. Wir können es
# verwenden, um unseren Codedeskriptiver und besser lesbar zu machen.

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

both_girl = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
        if younger == Kid.GIRL:
            both_girl +=1
            either_girl +=1
        else:
            either_girl+=1
    elif younger == Kid.GIRL:
        either_girl+=1

print(both_girl, older_girl, either_girl)
print("P(both | older): ", both_girl/older_girl)
print("P(both | either): ", both_girl/either_girl)