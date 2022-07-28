import unittest
from factory import factory
from models.country import Country
from orator_validator import ValidatorError
from config import db

class CountryTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from countries')

  def setUp(self):
    self.country = factory(Country).make()

  def testCountryMinimumViableData(self):
    self.assertTrue(self.country.save())

  def testCountryNameCannotBeBlank(self):
    self.country.name = ''
    with self.assertRaises(ValidatorError) as cm:
      self.country.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on name"}]')

  def testCountryNameMustBeString(self):
    self.country.name = 1
    with self.assertRaises(ValidatorError) as cm:
      self.country.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on name"}]')

if __name__ == '__main__':
  unittest.main()