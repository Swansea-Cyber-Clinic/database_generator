import unittest
from factory import factory
from models.police_force import PoliceForce
from orator_validator import ValidatorError
from config import db

class PoliceForceTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from police_forces')

  def setUp(self):
    self.police_force = factory(PoliceForce).make()
  
  def tearDown(self):
    db.delete('delete from police_forces')

  def testPoliceForceMinimumViableData(self):
    self.assertTrue(self.police_force.save())

  def testPoliceForceNameCannotBeBlank(self):
    self.police_force.name = ''
    with self.assertRaises(ValidatorError) as cm:
      self.police_force.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on name"}]')

  def testPoliceForceNameMustBeString(self):
    self.police_force.name = 1
    with self.assertRaises(ValidatorError) as cm:
      self.police_force.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on name"}]')

  def testPoliceForceDescriptionCannotBeBlank(self):
    self.police_force.description=''
    with self.assertRaises(ValidatorError) as cm:
      self.police_force.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on description"}]')

  def testPoliceForceDescriptionMustBeString(self):
    self.police_force.description = 1
    with self.assertRaises(ValidatorError) as cm:
      self.police_force.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on description"}]')

if __name__ == '__main__':
  unittest.main()