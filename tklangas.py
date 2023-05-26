from tkinter import *
from tkinter import messagebox, simpledialog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from viktorina_orm import Viktorina
from rezultatai import LaimetojuRezultatai

klausimu_kiekis = 3  # nurodyti skaiciu + 1
engine_viktorina = create_engine("sqlite:///viktorina.db", echo=False)
engine_rezultatai = create_engine("sqlite:///rezultatai.db", echo=False)
Session_viktorina = sessionmaker(bind=engine_viktorina)
Session_rezultatai = sessionmaker(bind=engine_rezultatai)
session_viktorina = Session_viktorina()
session_rezultatai = Session_rezultatai()
questions = session_viktorina.query(Viktorina).all()[:klausimu_kiekis]

langas = Tk()
current_question_index = 0
current_question = None
question_label = None
answer_buttons = []
dalyvio_vardas = None
surinkti_balai = 0

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

    if current_question_index < len(questions) - 1:
        # Gauti dabartinį klausimą iš sąrašo
        current_question = questions[current_question_index]

        # Rodyti klausimo ir atsakymų pasirinkimus
        question_label = Label(langas, text=current_question.question)
        question_label.pack()

        answer_options = [
            current_question.answer_1,
            current_question.answer_2,
            current_question.answer_3,
            current_question.answer_4,
        ]

        for i, answer_option in enumerate(answer_options):
            button = Button(langas, text=answer_option, command=lambda idx=i: patikrinti_atsakyma(idx))
            button.pack()
            answer_buttons.append(button)

        current_question_index += 1
    else:
        # Sąraše daugiau klausimų nėra
        messagebox.showinfo("Viktorina baigta", "Atsakėte į visus klausimus.")
        issaugoti_rezultatus()


def patikrinti_atsakyma(selected_index):
    global surinkti_balai
    selected_answer = selected_index + 1

    if selected_answer == current_question.correct_answer:
        surinkti_balai += 1
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
    session_rezultatai.add(rezultatas)
    session_rezultatai.commit()
    messagebox.showinfo("Rezultatai", "Jūsų rezultatas išsaugoti.")
    rezultatai()


def rezultatai():
    global pradeti_vel
    global iseiti
    iseiti = Button(langas, text="Iseiti", command=langas.quit)
    pradedi_vel = Button(
        langas,
        text="Bandyti dar karta",
        command=lambda: [pradedi_vel.pack_forget(), iseiti.pack_forget(), naikinti_rezultatus(), naujas_zaidimas()],
    )
    laimetojai = session_rezultatai.query(LaimetojuRezultatai).all()
    laimetojai.sort(key=lambda r: r.rezultatas, reverse=False)
    laimetojai = laimetojai[-10:]
    pradedi_vel.pack()
    iseiti.pack()
    for laimetojas in laimetojai:
        laimetojo_label = Label(langas, text=laimetojas.__str__())
        laimetojo_label.pack(side=BOTTOM)


def naikinti_rezultatus():
    for label in langas.winfo_children():
        if type(label) == Label:
            label.pack_forget()


def naujas_zaidimas():
    # global pradeti_vel
    # global iseiti
    # pradeti_vel_button.pack_forget()
    # iseiti_button.pack_forget()

    global questions
    questions = session_viktorina.query(Viktorina).all()[:klausimu_kiekis]
    global current_question_index
    current_question_index = 0
    global current_question
    current_question = None
    global question_label
    question_label = None
    global answer_buttons
    answer_buttons = []
    global dalyvio_vardas
    dalyvio_vardas = None
    global surinkti_balai
    surinkti_balai = 0
    klausimas()


klausimas()

langas.mainloop()
