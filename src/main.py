from src.Insect import Insect

if __name__ == "__main__":
    cockroach = Insect("cockroach", 4, True, False, False)
    fly = Insect("fly", 6, False, False, False)
    insects = [cockroach, fly, Insect.get_instance(), Insect.get_instance()]

    for insect in insects:
        print(insect)

    s1 = Insect.get_instance()
    s2 = Insect.get_instance()
    print(id(s1) == id(s2))

