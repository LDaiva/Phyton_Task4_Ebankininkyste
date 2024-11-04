from sqlalchemy.orm import sessionmaker

from models import engine, Person, Bank, Account

Session = sessionmaker(bind=engine)
session = Session()


def create_person(name, surname, social_security_no, phone_no):
    new_person = Person(
        name=name,
        surname=surname,
        social_security_no=social_security_no,
        phone_no=phone_no
    )
    session.add(new_person)
    session.commit()
    print(f"{new_person} added successful.")


def create_bank(name, address, swift_code):
    new_bank = Bank(
        name=name,
        address=address,
        swift_code=swift_code
    )
    session.add(new_bank)
    session.commit()
    print(f"{new_bank} added successful.")


def get_person(person_id):
    person = session.get(Person, person_id)
    if person:
        print(f"Get Person: {person}")
        return person
    else:
        print(f"Person code {person_id} doesn't exist")
        exit()


def get_bank(bank_id):
    bank = session.get(Bank, bank_id)
    if bank:
        print(f"Get Bank: {bank}")
        return bank
    else:
        print(f"Bank {bank_id} doesn't exist")
        exit()


def create_account(iban_no, person_id, bank_id):
    person = get_person(person_id)
    bank = get_bank(bank_id)
    new_account = Account(
        iban_no=f"{bank.name}-{iban_no}",
        person_id=person.id,
        bank_id=bank_id,
        person=person,
        bank=bank
    )
    session.add(new_account)
    session.commit()
    print(f"New Account: {new_account.id}: {new_account.iban_no}, {new_account.bank}, {new_account.person}")
    return new_account


def person_accounts(person_id):
    person = get_person(person_id)
    accounts = person.accounts
    for account in accounts:
        print(account)


# Testavimui atsikomentuoti funkcijų iškvietimus:
# P.S. person 'Pirmas', bank 'SEB' ir account 111 yra DB e-banks.sqlite lentelėse

# create_person('Pirmas','Pirmaitis','113456','+37066611111')
# create_person('Antras','Antrulis','223456','+37066622222')
# create_bank("SEB", "Adresas 1", "10008888")
# create_bank("Swedbank", "Adresas 2", "20008888")
# create_account(111, 1, 1)
# create_account(222, 2, 2)
# person_accounts(1)
# person_accounts(2)


