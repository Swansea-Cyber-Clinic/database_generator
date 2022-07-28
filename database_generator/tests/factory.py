from orator.orm import Factory
from models.police_force import PoliceForce
from models.organisation import Organisation
from models.country import Country
from models.category import Category

factory = Factory()

@factory.define(Organisation)
def organisation_factory(faker):
  return {
    'name': faker.name(),
    'description': faker.text()
  }

@factory.define(Country)
def country_factory(faker):
  return {
    'name': faker.country()
  }

@factory.define(Category)
def category_factory(faker):
  company = faker.company()
  return {
    'name': company[0:2],
    'description': company
  }

@factory.define(PoliceForce)
def police_force_factory(faker):
  return {
    'name': faker.company(),
    'description': faker.text()
  }