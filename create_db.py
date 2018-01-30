from app.app import db, Person
import random
import string
N_LETTERS = len(string.ascii_lowercase)

db.create_all()

def _random_name():
    return "".join(string.ascii_lowercase[random.randint(0, N_LETTERS-1)] for _ in range(20))


def main():
    for _ in range(10):
        id_ = random.randint(0, 100000000)
        age = random.randint(10, 50)
        name = _random_name()
        p = Person(id=id_, name=name, age=age)
        db.session.add(p)
    db.session.commit()

if __name__ == '__main__':
    main()