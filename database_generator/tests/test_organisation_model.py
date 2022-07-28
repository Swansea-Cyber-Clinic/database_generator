import unittest
from factory import factory
from models.organisation import Organisation
from orator_validator import ValidatorError
from config import db

class OrganisationTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from organisations')
  
  def setUp(self):
    self.organisation = factory(Organisation).make()

  def tearDown(self):
    db.delete('delete from organisations')

  def testOrganisationMinimumViableData(self):
    self.assertTrue(self.organisation.save())

  def testOrganisationNameCannotBeBlank(self):
    self.organisation.name = ''
    with self.assertRaises(ValidatorError) as cm:
      self.organisation.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on name"}]')

  def testOrganisationNameMustBeString(self):
    self.organisation.name = 1
    with self.assertRaises(ValidatorError) as cm:
      self.organisation.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on name"}]')

  def testOrganisationDescriptionCannotBeBlank(self):
    self.organisation.description=''
    with self.assertRaises(ValidatorError) as cm:
      self.organisation.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on description"}]')

  def testOrganisationDescriptionMustBeString(self):
    self.organisation.description = 1
    with self.assertRaises(ValidatorError) as cm:
      self.organisation.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on description"}]')

if __name__ == '__main__':
  unittest.main()