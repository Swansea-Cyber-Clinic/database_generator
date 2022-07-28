import unittest
from factory import factory
from models.category import Category
from orator_validator import ValidatorError
from config import db

class CategoryTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from categories')

  def setUp(self):
    self.category = factory(Category).make()
  
  def tearDown(self):
    db.delete('delete from categories')

  def testCategoryMinimumViableData(self):
    self.assertTrue(self.category.save())

  def testCategoryNameCannotBeBlank(self):
    self.category.name = ''
    with self.assertRaises(ValidatorError) as cm:
      self.category.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on name"}]')

  def testCategoryNameMustBeString(self):
    self.category.name = 1
    with self.assertRaises(ValidatorError) as cm:
      self.category.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on name"}]')

  def testCategoryDescriptionCannotBeBlank(self):
    self.category.description=''
    with self.assertRaises(ValidatorError) as cm:
      self.category.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Error of require on description"}]')

  def testCategoryDescriptionMustBeString(self):
    self.category.description = 1
    with self.assertRaises(ValidatorError) as cm:
      self.category.save()
    message = cm.exception.body
    self.assertEqual(message, '[{"msg": "Bad data type on description"}]')

if __name__ == '__main__':
  unittest.main()