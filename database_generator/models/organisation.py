from config import Model
from orator.orm import belongs_to_many
from orator_validator import Validator
from models.country import Country
from models.category import Category
from models.police_force import PoliceForce

class Organisation(Model, Validator):
  __guarded__ = []

  @belongs_to_many
  def countries(self):
    return Country

  @belongs_to_many
  def categories(self):
    return Category

  @belongs_to_many
  def police_forces(self):
    return PoliceForce

class OrganisationValidation(object):
  def creating(self, organisation):
    organisation.validate('name', require=True, data_type=str)
    organisation.validate('description', require=True, data_type=str)
    organisation.errors()

Organisation.observe(OrganisationValidation())