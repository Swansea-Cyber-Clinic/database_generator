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
    'description': faker.text(),
    'address_1': faker.street_address(),
    'address_2': faker.city(),
    'city': faker.city(),
    'postcode': faker.postcode(),
    'email_office': faker.ascii_company_email(),
    'email_help': faker.ascii_company_email(),
    'tel_office': faker.phone_number(),
    'tel_help': faker.phone_number()
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