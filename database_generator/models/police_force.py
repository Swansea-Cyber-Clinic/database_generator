from orator import Model
from orator_validator import Validator

class PoliceForce(Model, Validator):
  __guarded__ = []

class PoliceForceValidation(object):
  def saving(self, police_force):
    police_force.validate('name', require=True, data_type=str)
    police_force.validate('description', require=True, data_type=str)
    police_force.errors()

PoliceForce.observe(PoliceForceValidation())
