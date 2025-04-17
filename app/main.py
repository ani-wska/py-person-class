class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        partner_key = "wife" if "wife" in person_dict else "husband"
        partner_name = person_dict.get(partner_key)

        if partner_name:
            person = Person.people[name]
            person.partner = Person.people.get(partner_name)

    return list(Person.people.values())
