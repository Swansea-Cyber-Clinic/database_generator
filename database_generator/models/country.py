from orator import Model
from orator_validator import Validator


class Country(Model, Validator):
  __guarded__ = []
  __touches__ = ['organisations']

class CountryValidation(object):
  def creating(self, country):
    country.validate('name', require=True, data_type=str)
    country.errors()

Country.observe(CountryValidation())