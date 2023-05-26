from viktorina_orm import Viktorina, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    klausimas = input("Iveskite klausima: ")
    atsakymas_1 = input("Iveskite atsakyma 1: ")
    atsakymas_2 = input("Iveskite atsakyma 2: ")
    atsakymas_3 = input("Iveskite atsakyma 3: ")
    atsakymas_4 = input("Iveskite atsakyma 4: ")
    tesiginas_atsakymas = input("Iveskite teisinga atsakyma: ")
    viktorina = Viktorina(klausimas, atsakymas_1, atsakymas_2, atsakymas_3, atsakymas_4, tesiginas_atsakymas)
    session.add(viktorina)
    session.commit()
    testimas = input("Ar norite tęsti? (n)")
    if testimas:
        break
