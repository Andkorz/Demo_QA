import random

from data.data import Person
from faker import Faker

# faker_ru = Faker("ru_RU")
faker_en = Faker("en_US")
Faker.seed()


def generated_person():
    # person_ru = Person(
    #     full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
    #     firstname=faker_ru.first_name(),
    #     lastname=faker_ru.last_name(),
    #     age=random.randint(10, 80),
    #     department=faker_ru.job(),
    #     salary=random.randint(1000, 15880),
    #     email=faker_ru.email(),
    #     current_address=faker_ru.address(),
    #     permanent_address=faker_ru.address()
    # )

    person_en = Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(10, 80),
        department=faker_en.job(),
        salary=random.randint(1000, 15880),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
    )

    # yield person_ru
    yield person_en

def generated_file():
    path = rf"C:\Users\user\PycharmProjects\Demo_QA\filetest{random.randint(0, 999)}.txt"
    file = open(path, "w+")
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path

