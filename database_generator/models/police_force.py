from orator import Model
from orator_validator import Validator

class PoliceForce(Model, Validator):
  __guarded__ = []
  __touches__ = ['organisations']

class PoliceForceValidation(object):
  def creating(self, police_force):
    police_force.validate('name', require=True, data_type=str)
    police_force.validate('description', require=True, data_type=str)
    police_force.errors()

PoliceForce.observe(PoliceForceValidation())
