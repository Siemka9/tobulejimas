from sqlalchemy.orm import sessionmaker
from viktorina_orm import Viktorina, engine
from rezultatai import LaimetojuRezultatai


Session = sessionmaker(bind=engine)
session = Session()
viktorinos_duomenys = session.query(Viktorina).all()

atrinktos_eilutes = viktorinos_duomenys
taskai = 0

for eilute in atrinktos_eilutes:
    print("Klausimas: ")
    print(eilute.question)
    print("atsakymo variantai: ")
    print(f"1: {eilute.answer_1}")
    print(f"2: {eilute.answer_2}")
    print(f"3: {eilute.answer_3}")
    print(f"4: {eilute.answer_4}")

    atsakymas = int(input("Įrašykite teisingo atsakymo numerį: "))
    print(eilute.correct_answer, atsakymas)
    if atsakymas == eilute.correct_answer:
        print("Atsakymas teisingas")
        taskai += 1
    else:
        print("Atsakymas neteisingas")
    print("-------------------------------------------------")

print(f"Jūsų taškai: {taskai}")
print("-------------------------------------------------")
ar_issaugoti = input("Ar norite išsaugoti rezultatą? (taip/ne)")
if ar_issaugoti == "taip":
    vardas = input("Įveskite savo vardą: ")
    laimetojas = LaimetojuRezultatai(vardas, taskai)
    session.add(laimetojas)
    session.commit()
    print("Rezultatas išsaugotas")
input("Paspauskite ENTER, kad iseiti")
