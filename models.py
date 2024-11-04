from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///e-banks.sqlite")
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column("person_name", String)
    surname = Column(String)
    social_security_no = Column(Integer)
    phone_no = Column(String)

    accounts = relationship("Account", back_populates="person")

    def __repr__(self):
        return (f"a.k.:{self.id}, {self.name} {self.surname}, "
                f"soc.dr.: {self.social_security_no}, tel.: {self.phone_no}")


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column("bank_name", String)
    address = Column("bank_address", String)
    swift_code = Column(String)

    accounts = relationship("Account", back_populates="bank")

    def __repr__(self):
        return (
            f"{self.id}, {self.name} / {self.address} / {self.swift_code}")


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    iban_no = Column(Integer)
    balance = Column(Float)
    person_id = Column(Integer, ForeignKey("person.id"))
    bank_id = Column(Integer, ForeignKey("bank.id"))
    # Relationship one-to-many
    person = relationship("Person", back_populates='accounts')
    bank = relationship("Bank", back_populates='accounts')

    def __repr__(self):
        return (
            f"{self.person.name} {self.person.surname} {self.bank.name}- acc ID: {self.id}, balance: {self.balance} Eur")


Base.metadata.create_all(engine)
