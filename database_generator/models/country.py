from orator import Model
from orator_validator import Validator


class Country(Model, Validator):
  __guarded__ = []

class CountryValidation(object):
  def saving(self, country):
    country.validate('name', require=True, data_type=str)
    country.errors()

Country.observe(CountryValidation())