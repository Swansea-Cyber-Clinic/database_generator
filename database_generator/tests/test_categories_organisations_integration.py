import unittest
from factory import factory
from models.category import Category
from models.organisation import Organisation
from config import db

class CategoriesOrganisationsIntegrationTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from categories')
    db.delete('delete from organisations')

  def setUp(self):
    self.category = factory(Category).make()
    self.category.save()
    self.organisation = factory(Organisation).make()
    self.organisation.save()
    self.other_category = factory(Category).make()
    self.other_category.save()
  
  def tearDown(self):
    db.delete('delete from categories')
    db.delete('delete from organisations')

  def testAssociateCategoryWithOrganisation(self):
    self.assertTrue(self.organisation.categories().save(self.category), True)
    self.assertEqual(self.organisation.categories().count(), 1)

  def testOrganisationCanHaveMoreThanOneAssociatedCategory(self):
    self.assertTrue(self.organisation.categories().save(self.category), True)
    self.assertTrue(self.organisation.categories().save(self.other_category), True)
    self.assertEqual(self.organisation.categories().count(), 2)

if __name__ == '__main__':
  unittest.main()