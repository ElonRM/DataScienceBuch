def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


g = doubler(f1)
assert g(3) == 8, "(3+1) * 2 should equal 8"
assert g(-1) == 0, "(-1+1) * 2 should equal 0"

# das Klappt allerdings nicht bei Funktionen mit mehr als einem Argument:


def f2(x, y):
    return x + y


g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")


# Wir benötigen eine Möglichkeit, eine Funktion mit beliebig vielen Argumenten zu definieren.

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2")


def other_way_magic(x, y, z):
    return x+y+z


x_y_list = [1, 2]
z_dict = {"z": 3}

assert other_way_magic(*x_y_list, **z_dict) == 6, "1+2+3 should be 6"
print(*x_y_list)

# Wir werden damit aber lediglich Funktionen auf höherer ABstraktionsebene schreiben, die beliebige Argumente als Eingabe akzeptiert


def doubler_correct(f):
    """Funktioniert mit jeder Art von Eingabe f"""
    def g(*args, **kwargs):
        """Alle ARgumente von g werden direkt an f weitergereicht"""
        return 2 * f(*args, **kwargs)

    return g


g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"
