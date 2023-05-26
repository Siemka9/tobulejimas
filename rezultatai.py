# from sqlalchemy import Column, Integer, String, create_engine, Date
# from sqlalchemy.orm import declarative_base
# from datetime import date
#
# engine = create_engine('sqlite:///rezultatai.db', echo=False)
# Base = declarative_base()
#
#
# class LaimetojuRezultatai(Base):
#     __tablename__ = 'rezultatai'
#     __table_args__ = {'extend_existing': True}
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     result = Column(Integer)
#     time = Column(Date, default=date.today)
#
#     def __init__(self, name, result, time):
#         self.name = name
#         self.result = result
#         self.time = time
#
#     def __repr__(self):
#         return f"Vardas={self.name}, Rezultatas={self.result}, Laikas={self.time}"
#
#
# Base.metadata.create_all(engine)
