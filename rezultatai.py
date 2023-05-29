from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.orm import declarative_base
from datetime import date

engine = create_engine("sqlite:///rezultatai.db", echo=False)
Base = declarative_base()


class LaimetojuRezultatai(Base):
    __tablename__ = "rezultatai"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    rezultatas = Column(Integer)
    laikas = Column(Date, default=date.today)

    def __init__(self, vardas, rezultatas):
        self.vardas = vardas
        self.rezultatas = rezultatas

    def __repr__(self):
        return f"Vardas={self.vardas}, Rezultatas={self.rezultatas}, Laikas={self.laikas}"


Base.metadata.create_all(engine)
