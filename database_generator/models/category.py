from orator import Model
from orator_validator import Validator

class Category(Model, Validator):
  __guarded__ = []

class CategoryValidation(object):
  def saving(self, category):
    category.validate('name', require=True, data_type=str)
    category.validate('description', require=True, data_type=str)
    category.errors()

Category.observe(CategoryValidation())