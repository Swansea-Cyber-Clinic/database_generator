# not at all finished yet, code here is not refactored and only generates database containing data defined in the data directory
from config import db
from models.country import Country
from models.category import Category
from models.police_force import PoliceForce
from models.organisation import Organisation
import json

tables = [
  {
    'singular': 'category',
    'plural': 'categories',
  },
  {
    'singular': 'organisation',
    'plural': 'organisations',
  }
]

db.delete('delete from countries')
for t in tables:
  db.delete(f"delete from {t['plural']}")

with open('data/country.json', 'r') as cf:
  countries = json.load(cf)

with open('data/category.json', 'r') as cf:
  categories = json.load(cf)

with open('data/police_force.json', 'r') as cf:
  police_forces = json.load(cf)

for country in countries:
  Country.create(name=country)

for category in categories:
  Category.create(name=category['name'], description=category['description'])

for police_force in police_forces:
  PoliceForce.create(name=police_force['name'], description=police_force['description'])