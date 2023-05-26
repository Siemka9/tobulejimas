from tkinter import *
from tkinter import messagebox, simpledialog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from viktorina_orm import Viktorina, LaimetojuRezultatai

engine = create_engine('sqlite:///viktorina.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
questions = session.query(Viktorina).all()

langas = Tk()
current_question_index = 0  # Kad galėtu sekti dabartinį klausimą
current_question = None  # Kintamasis, skirtas išsaugoti dabartinį klausimą
question_label = None  # Kad būtų rodomas klausimo tekstas
answer_buttons = []  # Atsakymo parinkčių mygtukas
dalyvio_vardas = None
surinkti_balai = IntVar
paskutinis = StringVar()

langas.title("Testas")
uzrasas = Label(langas, text="Lietuvos salos")
uzrasas.pack()


def klausimas():
    global current_question
    global question_label
    global answer_buttons
    global current_question_index

    if current_question is not None:
        # Iš lango pašalinti ankstesnius klausimų ir atsakymų pasirinkimus
        question_label.pack_forget()
        for button in answer_buttons:
            button.pack_forget()

    if current_question_index < len(questions):
        # Gauti dabartinį klausimą iš sąrašo
        current_question = questions[current_question_index]

        # Rodyti klausimo ir atsakymų pasirinkimus
        question_label = Label(langas, text=current_question.question)
        question_label.pack()

        answer_options = [current_question.answer_1, current_question.answer_2, current_question.answer_3,
                          current_question.answer_4]

        for i, answer_option in enumerate(answer_options):
            button = Button(langas, text=answer_option, command=lambda idx=i: patikrinti_atsakyma(idx))
            button.pack()
            answer_buttons.append(button)

        current_question_index += 1
    else:
        # Sąraše daugiau klausimų nėra
        messagebox.showinfo("Viktorina baigta", "Atsakėte į visus klausimus.")


def patikrinti_atsakyma(selected_index):
    selected_answer = selected_index + 1

    if selected_answer == current_question.correct_answer:
        messagebox.showinfo("Teisingai", "Atsakymas teisingas!")
    else:
        messagebox.showinfo("Neteisingai", "Atsakymas neteisingas.")


    klausimas()


def issaugoti_rezultatus():
    global dalyvio_vardas
    global surinkti_balai

    if dalyvio_vardas is None:
        dalyvio_vardas = simpledialog.askstring("Participant's Name", "Įrašykite savo vardą:")

    rezultatas = LaimetojuRezultatai(vardas=dalyvio_vardas, rezultatas=surinkti_balai)
    session.add(rezultatas)
    session.commit()

    messagebox.showinfo("Rezultatai", "Jūsų rezultatas išsaugoti.")


klausimas()

langas.mainloop()
