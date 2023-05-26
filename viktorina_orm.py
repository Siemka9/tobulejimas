from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.orm import declarative_base
from datetime import date

engine = create_engine("sqlite:///viktorina.db", echo=False)
Base = declarative_base()


class Viktorina(Base):
    __tablename__ = "viktorina"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct_answer = Column(Integer)

    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, correct_answer):
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"Klausimas={self.question}, Pirmas_variantas={self.answer_1}, Antras_variantas={self.answer_2}, Trecias_variantas={self.answer_3}, Ketvirtas_variantas={self.answer_4}, Teisingas_atsakymas={self.correct_answer}"


# class LaimetojuRezultatai(Base):
#     __tablename__ = 'viktorina'
#     __table_args__ = {'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     vardas = Column(String)
#     rezultatas = Column(Integer)
#     laikas = Column(Date, default=date.today)
#
#
#     def __init__(self, vardas, rezultatas):
#         self.vardas = vardas
#         self.rezultatas = rezultatas
#
#
#     def __repr__(self):
#          return f"Vardas={self.vardas}, Rezultatas={self.rezultatas}, Laikas={self.laikas}"


Base.metadata.create_all(engine)
