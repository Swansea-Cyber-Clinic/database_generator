from orator import Model
from orator_validator import Validator

class Category(Model, Validator):
  __guarded__ = []
  __touches__ = ['organisations']

class CategoryValidation(object):
  def creating(self, category):
    category.validate('name', require=True, data_type=str)
    category.validate('description', require=True, data_type=str)
    category.errors()

Category.observe(CategoryValidation())