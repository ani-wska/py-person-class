class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = name
    pass


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_to_add = Person(person["name"], person["age"])
        if person.get("wife"):
            person_to_add.wife = person["wife"]
        elif person.get("husband"):
            person_to_add.husband = person["husband"]
        person_list.append(person_to_add)
    return person_list
