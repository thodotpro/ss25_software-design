# You are given the Person class and asked to write a ResponsiblePerson proxy that does the
# following:
# Allows person to drink unless they are Younger than 18 (in that case, return "too Young")
# Allows person to drive unless they are Younger than 16 (otherwise, "too Young")
# In case of driving while drink, returns "dead", regardless of age


from unittest import TestCase


class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'

class ResponsiblePerson:
  def __init__(self, person):
    self.person = person

  @property
  def age(self):
    return self.person.age
  
  @age.setter
  def age(self, value):
    self.person.age = value
  
  def drink(self):
    if self.person.age < 18:
      return 'too young'
    else:
      return self.person.drink()
  
  def drive(self):
    if self.person.age < 16:
      return 'too young'
    else:
      return self.person.drive()
  
  def drink_and_drive(self):
    return 'dead'



class Evaluate(TestCase):
  def test_exercise(self):
    p = Person(10)
    rp = ResponsiblePerson(p)

    self.assertEqual('too young', rp.drive())
    self.assertEqual('too young', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())

    rp.age = 20

    self.assertEqual('driving', rp.drive())
    self.assertEqual('drinking', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())

if __name__ == "__main__":
  test = Evaluate()
  test.test_exercise()

  # person1 = Person(16)
  # resp_person1 = ResponsiblePerson(person1)
  # print(resp_person1.drive())
  # print(resp_person1.drink())
  # print(resp_person1.drink_and_drive())
  # print("-------------")

  # resp_person1.age = 21

  # print(resp_person1.drive())
  # print(resp_person1.drink())
  # print(resp_person1.drink_and_drive())